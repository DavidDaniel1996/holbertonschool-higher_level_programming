-- Script that lists all records from second_table of hbnc_0c_0
-- Query lists all rows with name value, by highest score
SELECT 
    score,
    name 
FROM 
    second_table
WHERE EXISTS(
    SELECT name FROM second_table
)
ORDER BY 
    score DESC;
