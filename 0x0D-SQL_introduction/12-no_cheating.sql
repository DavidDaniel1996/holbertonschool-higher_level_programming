-- Script updates score of Bob to 10 in second_table of hbnc_0c_0
-- Query to update Bob's score
UPDATE second_table
SET
    score=10
WHERE
    name="Bob";
