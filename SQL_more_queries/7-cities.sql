-- Creates a database if doesn't exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Move to the created database
USE hbtn_0d_usa;

-- Creates a table named cities
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
