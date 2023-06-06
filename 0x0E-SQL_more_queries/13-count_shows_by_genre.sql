-- Script that lists all genres from hbtn_0d_tvshows and,
-- displays the number of shows linked to each show
SELECT g.`name` AS `genre_name`,
COUNT(*) AS `number_of_show_per_genre`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS t
ON g.`id` = t.`genre_id`
GROUP BY g.`name`
ORDER BY `number_of_show_per_genre` DESC;
