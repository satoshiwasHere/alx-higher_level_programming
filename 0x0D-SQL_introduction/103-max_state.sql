-- Import in hbtn_0c_0 database this table dump
-- script displays max temp of each state
-- ordred by state name

SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
