-- script Lists all genres in the database,
-- hbtn_0d_tvshows_rate by their rating.
-- ordered in descending rating.

SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS gn
       INNER JOIN `tv_show_genres` AS sh
       ON sh.`genre_id` = gn.`id`

       INNER JOIN `tv_show_ratings` AS sr
       ON sr.`show_id` = sh.`show_id`
 GROUP BY
`name`
 ORDER BY
`rating` DESC;
