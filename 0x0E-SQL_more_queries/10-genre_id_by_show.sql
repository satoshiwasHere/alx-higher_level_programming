-- Script lists all shows contained in hbtn_0d_tvshows
SELECT sh.`title`, gn.`genre_id`
  FROM `tv_shows` AS sh
        INNER JOIN `tv_show_genres` AS gn
	ON sh.`id` = gn.`show_id`
 ORDER BY sh.`title`, gn.`genre_id`;
