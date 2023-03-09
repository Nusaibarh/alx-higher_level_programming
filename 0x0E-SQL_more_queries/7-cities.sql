-- I want to create database
-- and also create a table in it

CREATE SCHEMA IF NOT EXISTS hbtn_0d_usa;

-- switch to database
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id));
