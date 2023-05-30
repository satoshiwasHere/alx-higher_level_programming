-- script lists no. of records with same score 
-- in 'second_table'
-- result should display 'score' with 'number' label
-- database hbtn_0c_0
SELECT score, COUNT('score') as number FROM second_table
GROUP BY score
ORDER BY score DESC;
