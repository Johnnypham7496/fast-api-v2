-- SQLite table creation (manual)

-- 1) VS Code - add extension SQLite (https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)
-- 2) create a blank file name it database.db
-- 3) the sql statement below will create a table with 3 records

-- create table statement
CREATE TABLE 'users' (
    'ID' INTEGER,
    'EMAIL' TEXT,
    'ROLE' TEXT,
    'USERNAME' TEXT,
    PRIMARY KEY(`ID`)
);

-- insert 3 records
INSERT INTO users VALUES(101, 'darth.vader@gmail.com', 'villian', 'darth.vader');
INSERT INTO users VALUES(102, 'super.man@gmail.com', 'hero', 'super.man');
INSERT INTO users VALUES(103, 'thor@gmail.com', 'hero', 'thor.odinson');

-- test if records are available
SELECT * FROM users