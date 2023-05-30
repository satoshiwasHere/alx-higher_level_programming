-- script listing records with 'score >= 10'
-- in the table 'second_table'
-- database 'hbtn_0c_0'
-- ordered list with 'SCORE' (top first)
SELECT score, name FROM second_table
WHERE score >= 10 ORDER BY score DESC;
