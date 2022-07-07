-- Script lists all cities
-- Query to select cities
SELECT c.id, c.name, s.name
FROM cities AS c
JOIN states AS s ON s.id = c.state_id
