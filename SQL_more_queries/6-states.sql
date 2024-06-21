-- Creates a database named hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Move to the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Creates a table in the hbtn_0d_usa database with the name states
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
