--- Delete database and add again
DROP DATABASE IF EXISTS fake_golf;
CREATE DATABASE fake_golf;
USE fake_golf;

--- Locations Lookup table
--- Stores list of locations
CREATE TABLE locations_lookup (
    id              INT             NOT NULL PRIMARY KEY AUTO_INCREMENT,
    location_name   VARCHAR(25)     NOT NULL,
    modifier_name   VARCHAR(25),
    special         VARCHAR(25),
    icon            VARCHAR(50),
    created_on      TIMESTAMP       NOT NULL DEFAULT NOW(),
    updated_on      TIMESTAMP       NOT NULL DEFAULT NOW() ON UPDATE NOW()
);

--- Status Lookup table
--- Stores status of tournaments
CREATE TABLE status_lookup (
    id          INT             NOT NULL PRIMARY KEY AUTO_INCREMENT,
    status_name VARCHAR(25)     NOT NULL,
    created_on  TIMESTAMP       NOT NULL DEFAULT NOW(),
    updated_on  TIMESTAMP       NOT NULL DEFAULT NOW() ON UPDATE NOW()
);

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
    designer_id     INT NOT NULL,
    course_image    VARCHAR(500),
    course_url      VARCHAR(500),
    par             INT             NOT NULL,
    yardage         INT             NOT NULL,
    expected_par    DECIMAL(4,2),
    scratch_par     INT,
    created_on      TIMESTAMP       NOT NULL DEFAULT NOW(),
    updated_on      TIMESTAMP       NOT NULL DEFAULT NOW() ON UPDATE NOW()
);

--- Courses Trees table
--- Gives results for shots from trees. Because each course can be different,
---     we store these with courses.id
CREATE TABLE courses_trees (
    id                      INT         NOT NULL PRIMARY KEY AUTO_INCREMENT,
    course_id               INT         NOT NULL,
    curr_location_id        INT         NOT NULL,
    start_diff              INT         NOT NULL,
    end_diff                INT         NOT NULL,
    new_location_id_par4    INT         NOT NULL,
    new_location_id_par5    INT         NOT NULL,
    created_on              TIMESTAMP   NOT NULL DEFAULT NOW(),
    updated_on              TIMESTAMP   NOT NULL DEFAULT NOW() ON UPDATE NOW()
);

--- Courses Putting table
--- Gives results for putting. Because each course can be different,
---     we store these with courses.id
CREATE TABLE courses_putting (
    id                  INT         NOT NULL PRIMARY KEY AUTO_INCREMENT,
    course_id           INT         NOT NULL,
    curr_location_id    INT         NOT NULL,
    start_diff          INT         NOT NULL,
    end_diff            INT         NOT NULL,
    new_location_id     INT         NOT NULL,
    created_on          TIMESTAMP   NOT NULL DEFAULT NOW(),
    updated_on          TIMESTAMP   NOT NULL DEFAULT NOW() ON UPDATE NOW()
);

--- Holes table
--- Stores data on individual holes for courses
CREATE TABLE holes (
    id              INT             NOT NULL PRIMARY KEY AUTO_INCREMENT,
    course_id       INT             NOT NULL,
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
    id                  INT         NOT NULL PRIMARY KEY AUTO_INCREMENT,
    hole_id             INT         NOT NULL,
    curr_location_id    INT         NOT NULL,
    start_diff          INT         NOT NULL,
    end_diff            INT         NOT NULL,
    new_location_id     INT         NOT NULL,
    created_on          TIMESTAMP   NOT NULL DEFAULT NOW(),
    updated_on          TIMESTAMP   NOT NULL DEFAULT NOW() ON UPDATE NOW()
);

--- Tournaments
--- List of tournaments
CREATE TABLE tournaments (
    id                  INT             NOT NULL PRIMARY KEY AUTO_INCREMENT,
    tournament_name     VARCHAR(100)    NOT NULL,
    designer_id         INT NOT NULL,
    tournament_image    VARCHAR(500),
    created_on          TIMESTAMP       NOT NULL DEFAULT NOW(),
    updated_on          TIMESTAMP       NOT NULL DEFAULT NOW() ON UPDATE NOW()
);

--- Tournament Rounds
--- Lists rounds of a tournament
CREATE TABLE tournament_rounds (
    id              INT         NOT NULL PRIMARY KEY AUTO_INCREMENT,
    tournament_id   INT         NOT NULL,
    round           INT         NOT NULL,
    course_id       INT         NOT NULL,
    created_on      TIMESTAMP   NOT NULL DEFAULT NOW(),
    updated_on      TIMESTAMP   NOT NULL DEFAULT NOW() ON UPDATE NOW()
);

--- Tournament Targets
--- Lists target shots for each hole in a tournament round
CREATE TABLE tournament_targets (
    id                      INT         NOT NULL PRIMARY KEY AUTO_INCREMENT,
    round_id                INT         NOT NULL,
    hole                    INT         NOT NULL,
    shot_1                  INT,
    shot_2                  INT,
    shot_3                  INT,
    shot_4                  INT,
    shot_5                  INT,
    shot_6                  INT,
    shot_7                  INT,
    shot_8                  INT,
    shot_9                  INT,
    tournament_status_id    INT         NOT NULL,
    created_on              TIMESTAMP   NOT NULL DEFAULT NOW(),
    updated_on              TIMESTAMP   NOT NULL DEFAULT NOW() ON UPDATE NOW()
);

--- Locations Lookup Values
INSERT INTO locations_lookup (id, location_name, modifier_name, special, icon) VALUES
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
    (11, "Greenside", "Trees", "trees", "trees"),
    (12, "Third", "Fairway", NULL, "fairway"),
    (13, "Third", "Rough", "rough", "rough"),
    (14, "Third", "Bunker", "bunker", "bunker"),
    (15, "Third", "Trees", "trees", "trees"),
    (16, "Second", "Fairway", NULL, "fairway"),
    (17, "Second", "Rough", "rough", "rough"),
    (18, "Second", "Bunker", "bunker", "bunker"),
    (19, "Second", "Trees", "trees", "trees"),
    (20, "Out of Bounds", NULL, "oob", "oob"),
    (21, "Water", NULL, "water", "water"),
    (22, "Tee Box", NULL, NULL, "tee")
;

--- Status Lookup Values
INSERT INTO status_lookup (id, status_name) VALUES
    (1, "Setting Up"),
    (2, "Active"),
    (3, "Completed"),
    (4, "Canceled")
;

--- Icon links
--- https://www.flaticon.com/packs/golf-76?word=golf