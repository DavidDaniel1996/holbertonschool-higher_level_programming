-- Script creates database 'hbtn_0d_2' and user 'user_0d_2'
-- Query to create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Query to create user and set password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Query to set SELECT privileges for user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
