-- script uses the hbtn_0d_tvshows database to list all genres,
-- not linked to the show Dexter
SELECT DISTINCT
`name`
  FROM `tv_genres` AS gn
       INNER JOIN `tv_show_genres` AS sh
       ON gn.`id` = sh.`genre_id`

       INNER JOIN `tv_shows` AS ts
       ON sh.`show_id` = ts.`id`
       WHERE gn.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` AS gn
	             INNER JOIN `tv_show_genres` AS sh
		     ON gn.`id` = sh.`genre_id`

		     INNER JOIN `tv_shows` AS ts
		     ON sh.`show_id` = ts.`id`
		     WHERE ts.`title` = "Dexter")
 ORDER BY
gn.`name`;
