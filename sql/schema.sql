CREATE TABLE users(
    username     VARCHAR(20)     PRIMARY KEY NOT NULL,
    password     VARCHAR(256)    NOT NULL,
    type         VARCHAR(1)      NOT NULL,
    created      TIMESTAMP       DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE admin(
    username    VARCHAR(20)     PRIMARY KEY NOT NULL,
    firstname   VARCHAR(20)     PRIMARY KEY NOT NULL,
    lastname    VARCHAR(256)    NOT NULL

    CONSTRAINT fk_user
        FOREIGN KEY (username)
        REFERENCES users (username)
        ON DELETE CASCADE
);

CREATE TABLE parent(
    username    VARCHAR(20)     PRIMARY KEY NOT NULL,
    firstname   VARCHAR(20)     NOT NULL,
    lastname    VARCHAR(256)    NOT NULL,


    CONSTRAINT fk_user
        FOREIGN KEY (username)
        REFERENCES users (username)
        ON DELETE CASCADE
);

CREATE TABLE student(
    username        VARCHAR(20)     PRIMARY KEY NOT NULL,
    firstname       VARCHAR(20)     NOT NULL,
    lastname        VARCHAR(256)    NOT NULL,
    middleinitial   
    

    CONSTRAINT fk_user
        FOREIGN KEY (username)
        REFERENCES users (username)
        ON DELETE CASCADE
);