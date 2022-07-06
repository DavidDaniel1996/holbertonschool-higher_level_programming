-- Script lists all records >= 10 in second_table of hbnc_0c_0
-- Query to list records in 'score, name' format by highest score
SELECT score, name FROM second_table WHERE score >=10 ORDER BY score DESC;
