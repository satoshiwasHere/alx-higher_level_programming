-- script lists all Comedy shows in the database hbtn_0d_tvshows
-- arranged in descending order
SELECT
ts.`title`
  FROM `tv_shows` AS ts
       INNER JOIN `tv_show_genres` AS sh
       ON ts.`id` = sh.`show_id`

       INNER JOIN `tv_genres` AS gn
       ON gn.`id` = sh.`genre_id`
       WHERE gn.`name` = "Comedy"
 ORDER BY
ts.`title`;
