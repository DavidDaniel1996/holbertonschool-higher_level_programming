-- Script that lists all records from second_table of hbnc_0c_0
-- Query lists all rows with name value, by highest score
SELECT 
    score,
    name 
FROM 
    second_table
WHERE
    name IS NOT NULL
ORDER BY 
    score DESC;
