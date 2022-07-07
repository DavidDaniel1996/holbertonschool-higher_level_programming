-- Script creates database 'hbtn_0d_usa' and table 'cties'
-- Query creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Query to create 'states'
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT AUTO_INCREMENT,
    state_id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
