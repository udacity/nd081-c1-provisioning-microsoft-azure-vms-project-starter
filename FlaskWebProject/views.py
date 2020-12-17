"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect, request, session, url_for
from werkzeug.urls import url_parse
from config import Config
from FlaskWebProject import app, db
from FlaskWebProject.forms import LoginForm, PostForm
from flask_login import current_user, login_user, logout_user, login_required
from FlaskWebProject.models import User, Post
import msal
import uuid

imageSourceUrl = 'https://' + app.config['BLOB_ACCOUNT'] + '.blob.core.windows.net/' + app.config[
    'BLOB_CONTAINER'] + '/'


@app.route('/')
@app.route('/home')
@login_required
def home():
    """
    Used to display home page
    :return: Home template
    """
    user = User.query.filter_by(username=current_user.username).first_or_404()
    posts = Post.query.all()
    return render_template(
        'index.html',
        title='Home Page',
        posts=posts
    )


@app.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    """
    Used to create a new post
    :return: home template
    """
    form = PostForm(request.form)
    if form.validate_on_submit():
        post = Post()
        post.save_changes(form, request.files['image_path'], current_user.id, new=True)
        return redirect(url_for('home'))
    return render_template(
        'post.html',
        title='Create Post',
        imageSource=imageSourceUrl,
        form=form
    )


@app.route('/post/<int:id>', methods=['GET', 'POST'])
@login_required
def post(id):
    """
    Used to edit post
    :param id:
    :return: Home template
    """
    post = Post.query.get(int(id))
    form = PostForm(formdata=request.form, obj=post)
    if form.validate_on_submit():
        post.save_changes(form, request.files['image_path'], current_user.id)
        return redirect(url_for('home'))
    return render_template(
        'post.html',
        title='Edit Post',
        imageSource=imageSourceUrl,
        form=form
    )


@app.route('/deletepost/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_post(id):
    """
    Used to delete posts
    :param id:
    :return: Home template
    """
    post = Post.query.get(int(id))
    if post:  # if post with id exists delete it
        # Delete the blob
        delete_blob = post.delete_blobs(post.image_path)
        if delete_blob:
            # TODO: Delete post
            db.session.delete(post)
            db.session.commit()
        else:
            flash('Blob was not deleted and hence post wasn\'t deleted!')
    posts = Post.query.all()
    return render_template(
        'index.html',
        title='Home Page',
        posts=posts
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Used to login user
    :return: # TODO: complete this
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            app.logger.warning('%s Failed login: Invalid credentials')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        # INFO: Added logs for user logins
        app.logger.info('%s logged in successfully at ', user.username)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    session["state"] = str(uuid.uuid4())
    auth_url = _build_auth_url(scopes=Config.SCOPE, state=session["state"])
    return render_template('login.html', title='Sign In', form=form, auth_url=auth_url)


@app.route(Config.REDIRECT_PATH)  # Its absolute URL must match your app's redirect_uri set in AAD
def authorized():
    """
    Used to authorize user using ADD
    :return: Redirect to home page
    """
    if request.args.get('state') != session.get("state"):
        return redirect(url_for("home"))  # No-OP. Goes back to Index page
    if "error" in request.args:  # Authentication/Authorization failure
        return render_template("auth_error.html", result=request.args)
    if request.args.get('code'):
        cache = _load_cache()
        # TODO: Acquire a token from a built msal app, along with the appropriate redirect URI
        result = _build_msal_app(cache=cache).acquire_token_by_authorization_code(
            request.args['code'], scopes=Config.SCOPE,
            redirect_uri=url_for('authorized', _external=True, _scheme='https')
        )
        if "error" in result:
            return render_template("auth_error.html", result=result)
        session["user"] = result.get("id_token_claims")
        # Note: In a real app, we'd use the 'name' property from session["user"] below
        # Here, we'll use the admin username for anyone who is authenticated by MS
        user = User.query.filter_by(username=session["user"]).first()
        login_user(user)
        _save_cache(cache)
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    """
    Used to logout user
    :return: Redirect to login page
    """
    app.logger.info('%s Successfully logged out at ', current_user)
    logout_user()
    if session.get("user"):  # Used MS Login
        # Wipe out user and its token cache from session
        session.clear()
        # Also logout from your tenant's web session
        return redirect(
            Config.AUTHORITY + "/oauth2/v2.0/logout" +
            "?post_logout_redirect_uri=" + url_for("login", _external=True))

    return redirect(url_for('login'))


def _load_cache():
    """
    Used to load cached Microsoft mail
    account user's credentials
    :return: The stored cache
    """
    # TODO: Load the cache from `msal`, if it exists
    cache = msal.SerializableTokenCache()
    if session.get('token_cache'):
        cache.deserialize(session['token_cache'])
    return cache


def _save_cache(cache):
    """
    Used to cache user information
    :param cache:
    :return: Nothid
    """
    # TODO: Save the cache, if it has changed
    if cache.has_state_changed:
        session['token_cache'] = cache.serialize()


def _build_msal_app(cache=None, authority=None):
    """
    Used to build a Microsoft Authentication Library
    client object
    :param cache:
    :param authority:
    :return: ConfidentialClientApplication
    """
    # TODO: Return a ConfidentialClientApplication
    return msal.ConfidentialClientApplication(
        Config.CLIENT_ID, authority=authority or Config.AUTHORITY,
        client_credential=Config.CLIENT_SECRET, token_cache=cache
    )


def _build_auth_url(authority=None, scopes=None, state=None):
    """
    Used to build the auth request url
    :param authority:
    :param scopes:
    :param state:
    :return: The full Auth Request URL
    """
    # TODO: Return the full Auth Request URL with appropriate Redirect URI
    return _build_msal_app(authority=authority).get_authorization_request_url(
        scopes or [], state=state or str(uuid.uuid4()),
        redirect_uri=url_for('authorized', _external=True, _scheme='https')
    )
