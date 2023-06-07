-- Script that lists all genres from hbtn_0d_tvshows and,
-- displays the number of shows linked to each show
SELECT
gn.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS gn
       INNER JOIN `tv_show_genres` AS ts
       ON gn.`id` = ts.`genre_id`
 GROUP BY gn.`name`
 ORDER BY
`number_of_shows` DESC;
