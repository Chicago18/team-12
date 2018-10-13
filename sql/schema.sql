CREATE TABLE user(
    username     VARCHAR(20)     PRIMARY KEY NOT NULL,
    password     VARCHAR(256)    NOT NULL,
    type         VARCHAR(1)      NOT NULL,
    created      TIMESTAMP       DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE admin(
    username    VARCHAR(20)     PRIMARY KEY NOT NULL,
    firstname   VARCHAR(20)     NOT NULL,
    lastname    VARCHAR(256)    NOT NULL
);

CREATE TABLE parent(
    username        VARCHAR(20)     PRIMARY KEY NOT NULL,
    firstname       VARCHAR(20)     NOT NULL,
    lastname        VARCHAR(256)    NOT NULL,
    familytype      VARCHAR(50)     NOT NULL,
    housingstatus   VARCHAR(50)     NOT NULL,
    foodstamps      VARCHAR(3)      NOT NULL,
    reducedlunch    VARCHAR(3)      NOT NULL,
    insurance       VARCHAR(3)      NOT NULL,
    referral        VARCHAR(256)    NOT NULL,
    clientid        int,
    incomesource1   CHAR(1)         NOT NULL,
    incomesource2   CHAR(1)         NOT NULL,
    incomesource3   CHAR(1)         NOT NULL,    
    incomesource4   CHAR(1)         NOT NULL,
    incomesource5   CHAR(1)         NOT NULL,
    incomesource6   CHAR(1)         NOT NULL,
    incomesource7   CHAR(1)         NOT NULL,
    incomesource8   CHAR(1)         NOT NULL
);

CREATE TABLE student(
    username        VARCHAR(20)     PRIMARY KEY NOT NULL,
    firstname       VARCHAR(20)     NOT NULL,
    lastname        VARCHAR(256)    NOT NULL,
    middleinitial   VARCHAR(1),
    parentid        VARCHAR(20)     NOT NULL,
    gender          VARCHAR(6)      NOT NULL,
    age             int             NOT NULL,
    birthdate       TIMESTAMP       NOT NULL,
    phonenumber     VARCHAR(10)     NOT NULL,
    ethnicity       VARCHAR(20)     NOT NULL,
    race            VARCHAR(256)    NOT NULL,
    currentgrade    VARCHAR(5)      NOT NULL,
    school          VARCHAR(256)    NOT NULL,
    disability      VARCHAR(50),     
    communityarea   VARCHAR(256),    
    ward            VARCHAR(256),
    registered      VARCHAR(1)      NOT NULL
);