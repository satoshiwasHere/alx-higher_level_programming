-- import in hbtn_0c_0 database this table dump
-- script displaying average temp(fahr) by city

SELECT city,
AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC;
