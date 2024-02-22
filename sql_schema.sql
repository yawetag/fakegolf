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