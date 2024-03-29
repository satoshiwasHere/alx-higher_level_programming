-- Import in hbtn_0c_0 database this table dump
-- script displays the temp of 3 cities in,
-- july and August
-- ordered by temperature (descending)

SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
