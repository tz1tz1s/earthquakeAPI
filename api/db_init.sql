CREATE TABLE IDS (
    ID INT NOT NULL,
    PRIMARY KEY (ID),
    UNIQUE (ID)
);

CREATE TABLE mag (
    ID INT(255) ,
    UNIQUE (ID),
    magnitude INT(255),
    parent_id INT(255),
    FOREIGN KEY (parent_id)
         REFERENCES ids(id)
         ON DELETE CASCADE

);

CREATE TABLE place (
    ID INT(255) ,
    UNIQUE (ID),
    City VARCHAR(65535),
    parent_id INT(255),
    FOREIGN KEY (parent_id)
         REFERENCES ids(id)
         ON DELETE CASCADE

);

CREATE TABLE time_stamp (
    ID INT(255) ,
    UNIQUE (ID),
    City INT(255),
    parent_id INT(255),
    FOREIGN KEY (parent_id)
         REFERENCES ids(id)
         ON DELETE CASCADE

);

CREATE TABLE updated (
    ID INT(255) ,
    UNIQUE (ID),
    updated INT(255),
    parent_id INT(255),
    FOREIGN KEY (parent_id)
         REFERENCES ids(id)
         ON DELETE CASCADE

);
CREATE TABLE timezone (
    ID INT(255) ,
    UNIQUE (ID),
    timezone INT(255),
    parent_id INT(255),
    FOREIGN KEY (parent_id)
         REFERENCES ids(id)
         ON DELETE CASCADE

);

CREATE TABLE url (
    ID INT(255) ,
    UNIQUE (ID),
    url VARCHAR(65535),
    parent_id INT(255),
    FOREIGN KEY (parent_id)
         REFERENCES ids(id)
         ON DELETE CASCADE

);

CREATE TABLE detail (
    ID INT(255) ,
    UNIQUE (ID),
    details VARCHAR(65535),
    parent_id INT(255),
    FOREIGN KEY (parent_id)
         REFERENCES ids(id)
         ON DELETE CASCADE

);
