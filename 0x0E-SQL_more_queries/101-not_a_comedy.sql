-- script lists all shows without genre Comedy in the database hbtn_0d_tvshows
SELECT DISTINCT
`title`
  FROM `tv_shows` AS ts
       LEFT JOIN `tv_show_genres` AS sh
       ON sh.`show_id` = ts.`id`

       LEFT JOIN `tv_genres` AS gn
       ON gn.`id` = sh.`genre_id`
       WHERE ts.`title` NOT IN
             (SELECT `title`
                FROM `tv_shows` AS ts
	             INNER JOIN `tv_show_genres` AS sh
		     ON sh.`show_id` = ts.`id`

		     INNER JOIN `tv_genres` AS gn
		     ON gn.`id` = sh.`genre_id`
		     WHERE gn.`name` = "Comedy")
 ORDER BY
`title`;
