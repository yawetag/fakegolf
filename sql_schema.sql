--- Delete database and add again
DROP DATABASE IF EXISTS fake_golf;
CREATE DATABASE fake_golf;
USE fake_golf;

--- Users table
--- Tracks the information of the players in the game
CREATE TABLE users (
	id 					INT				NOT NULL PRIMARY KEY AUTO_INCREMENT,
    player_name 		VARCHAR(40)		NOT NULL,
    discord_snowflake	VARCHAR(20),
    is_admin 			BOOLEAN			NOT NULL DEFAULT 0,
    is_official 		BOOLEAN			NOT NULL DEFAULT 0,
    created_on 			TIMESTAMP		NOT NULL DEFAULT NOW(),
    updated_on 			TIMESTAMP		NOT NULL DEFAULT NOW() ON UPDATE NOW()
);

--- Courses table
--- Stores data on courses
CREATE TABLE courses (
    id              INT             NOT NULL PRIMARY KEY AUTO_INCREMENT,
    course_name     VARCHAR(100)    NOT NULL,
    designer        INT NOT NULL,
    course_image    VARCHAR(500),
    course_url      VARCHAR(500),
    par             INT             NOT NULL,
    yardage         INT             NOT NULL,
    expected_par    DECIMAL(4,2),
    scratch_par     INT,
    created_on      TIMESTAMP       NOT NULL DEFAULT NOW(),
    updated_on      TIMESTAMP       NOT NULL DEFAULT NOW() ON UPDATE NOW()
);

--- Holes table
--- Stores data on individual holes for courses
CREATE TABLE holes (
    id              INT             NOT NULL PRIMARY KEY AUTO_INCREMENT,
    course          INT             NOT NULL,
    hole            INT             NOT NULL,
    hole_image      VARCHAR(500),
    hole_url        VARCHAR(500),
    par             INT             NOT NULL,
    yardage         INT             NOT NULL,
    expected_par    DECIMAL(4,2),
    scratch_par     INT,
    created_on      TIMESTAMP       NOT NULL DEFAULT NOW(),
    updated_on      TIMESTAMP       NOT NULL DEFAULT NOW() ON UPDATE NOW()
);

--- Hole Shots table
--- Stores each hole's shot information.
CREATE TABLE hole_shots (
    id              INT         NOT NULL PRIMARY KEY AUTO_INCREMENT,
    hole            INT         NOT NULL,
    curr_location   INT         NOT NULL,
    start_diff      INT         NOT NULL,
    end_diff        INT         NOT NULL,
    new_location    INT         NOT NULL,
    created_on      TIMESTAMP   NOT NULL DEFAULT NOW(),
    updated_on      TIMESTAMP   NOT NULL DEFAULT NOW() ON UPDATE NOW()
);

--- Locations Lookup table
--- Stores list of locations
CREATE TABLE locations (
    id          INT             NOT NULL PRIMARY KEY AUTO_INCREMENT,
    location    VARCHAR(25)     NOT NULL,
    modifier    VARCHAR(25),
    special     VARCHAR(25),
    icon        VARCHAR(50),
    created_on  TIMESTAMP       NOT NULL DEFAULT NOW(),
    updated_on  TIMESTAMP       NOT NULL DEFAULT NOW() ON UPDATE NOW()
);

--- Courses Trees table
--- Gives results for shots from trees. Because each course can be different,
---     we store these with courses.id
CREATE TABLE courses_trees (
    id              INT         NOT NULL PRIMARY KEY AUTO_INCREMENT,
    course          INT         NOT NULL,
    curr_location   INT         NOT NULL,
    start_diff      INT         NOT NULL,
    end_diff        INT         NOT NULL,
    new_location_4  INT         NOT NULL,
    new_location_5  INT         NOT NULL,
    created_on      TIMESTAMP   NOT NULL DEFAULT NOW(),
    updated_on      TIMESTAMP   NOT NULL DEFAULT NOW() ON UPDATE NOW()
);

--- Courses Putting table
--- Gives results for putting. Because each course can be different,
---     we store these with courses.id
CREATE TABLE courses_putting (
    id              INT         NOT NULL PRIMARY KEY AUTO_INCREMENT,
    course          INT         NOT NULL,
    curr_location   INT         NOT NULL,
    start_diff      INT         NOT NULL,
    end_diff        INT         NOT NULL,
    new_location    INT         NOT NULL,
    created_on      TIMESTAMP   NOT NULL DEFAULT NOW(),
    updated_on      TIMESTAMP   NOT NULL DEFAULT NOW() ON UPDATE NOW()
);

--- Locations Values
INSERT INTO locations (id, location, modifier, special, icon) VALUES
    (1, "In the hole", NULL, NULL, "hole"),
    (2, "Green", "Close", NULL, "green"),
    (3, "Green", "Short", NULL, "green"),
    (4, "Green", "Average", NULL, "green"),
    (5, "Green", "Medium", NULL, "green"),
    (6, "Green", "Long", NULL, "green"),
    (7, "Green", "Super Long", NULL, "green"),
    (8, "Greenside", "Fairway", NULL, "fairway"),
    (9, "Greenside", "Rough", "rough", "rough"),
    (10, "Greenside", "Bunker", "bunker", "bunker"),
    (11, "Third", "Fairway", NULL, "fairway"),
    (12, "Third", "Rough", "rough", "rough"),
    (13, "Third", "Bunker", "bunker", "bunker"),
    (14, "Third", "Trees", "trees", "trees"),
    (15, "Second", "Fairway", NULL, "fairway"),
    (16, "Second", "Rough", "rough", "rough"),
    (17, "Second", "Bunker", "bunker", "bunker"),
    (18, "Second", "Trees", "trees", "trees"),
    (19, "Out of Bounds", NULL, "oob", "oob"),
    (20, "Water", NULL, "water", "water"),
    (21, "Tee Box", NULL, NULL, "tee")
;

--- Icon links
--- https://www.flaticon.com/packs/golf-76?word=golf