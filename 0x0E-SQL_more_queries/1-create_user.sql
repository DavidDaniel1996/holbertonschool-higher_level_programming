-- Script to create user 'user_0d_1' with all privileges and password set
-- Query to create user and set password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Query to grant all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
