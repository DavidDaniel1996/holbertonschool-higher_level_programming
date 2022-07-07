-- Script creates table 'unique_id'
-- Query to create table with unique constraint
CREATE TABLE IF NOT EXISTS unique_id(
    id INT,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT UC_unique_id UNIQUE (id)
);
-- Query sets id default value to 1
ALTER TABLE unique_id ALTER COLUMN id SET DEFAULT 1;
