# Azure will require tests in order to deploy the app.
# Feel free to add your own that actually test functionality.
def add(a):
    return a + 1

def test_add_function():
    assert add(1) == 2
