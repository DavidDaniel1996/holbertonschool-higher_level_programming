-- Script creates database 'hbtn_0d_usa' and table 'states'
-- Query creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Query to create 'states'
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INT AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT PK_states PRIMARY KEY (id)
);
