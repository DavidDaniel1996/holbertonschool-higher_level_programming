-- Script lists number of records with same score from second_table of hbnc_0c_0
-- Query lists scores and times repeated, starting with most repeated
SELECT
    score,
    COUNT(score) AS number
FROM
    second_table
GROUP BY score
ORDER BY number DESC;
