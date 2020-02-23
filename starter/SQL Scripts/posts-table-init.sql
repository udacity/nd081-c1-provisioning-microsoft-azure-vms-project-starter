CREATE TABLE POSTS(
    id INT NOT NULL IDENTITY(1, 1),
    title VARCHAR(150) NOT NULL,
    author VARCHAR(75) NOT NULL,
	body VARCHAR(800) NOT NULL,
	image_path VARCHAR(100) NULL,
	timestamp DATETIME NOT NULL DEFAULT(GETDATE()),
	user_id INT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO dbo.posts (title, author, body, user_id)
VALUES (
    'Lorem ipsum dolor sit amet',
    'John Smith',
    'Proin sit amet mi ornare, ultrices augue quis, facilisis tellus. Quisque neque dui, tincidunt sed volutpat quis, maximus sed est. Sed justo orci, rhoncus ac nulla eu, rhoncus luctus justo. Etiam maximus, felis eu varius fermentum, libero orci egestas purus, id condimentum mauris orci nec nibh. Vivamus risus ipsum, semper vel nibh in, suscipit commodo massa. Suspendisse non velit vitae neque condimentum viverra vel eget enim. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Vivamus fermentum sagittis ligula et fringilla. Aenean nec lacinia lacus.',
    1
);