-- Script creates table 'id_not_null'
-- Query to create table
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT,
    name VARCHAR(256) NOT NULL
);
-- Query sets id default value to 1
ALTER TABLE id_not_null ALTER COLUMN id SET DEFAULT 1;
