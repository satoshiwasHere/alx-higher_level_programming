-- script that lists all shows contained in the database hbtn_0d_tvshows
SELECT
sh.`title`, gn.`genre_id`
  FROM `tv_shows` AS sh
       LEFT JOIN `tv_show_genres` AS gn
       ON sh.`id` = gn.`show_id`
 ORDER BY
sh.`title`, gn.`genre_id`;
 
