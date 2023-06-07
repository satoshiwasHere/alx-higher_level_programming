-- script lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- ordered by ascending genre name.
SELECT
gn.`name`
  FROM `tv_genres` AS gn
       INNER JOIN `tv_show_genres` AS sh
       ON gn.`id` = sh.`genre_id`

       INNER JOIN `tv_shows` AS ts
       ON ts.`id` = sh.`show_id`
       WHERE ts.`title` = "Dexter"
 ORDER BY
gn.`name`;
