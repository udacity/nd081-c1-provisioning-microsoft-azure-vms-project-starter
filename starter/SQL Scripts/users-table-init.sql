CREATE TABLE USERS (
    id INT NOT NULL IDENTITY(1, 1),
    username VARCHAR(64) NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO dbo.users (username, password_hash)
VALUES ('admin', 'pbkdf2:sha256:150000$QlIrz6Hg$5f4cd25d78a6c79906a53f74ef5d3bb2609af2b39d9e5dd6f3beabd8c854dd60')