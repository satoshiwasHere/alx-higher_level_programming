-- script lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- ordered by ascending genre name.
SELECT 
g.`genre_name`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS s
       ON g.`genre_id` = s.`genre_id`
       INNER JOIN `tv_shows` AS t
       ON t.`id` = s.`show_id`
       WHERE t.`title` = "Dexter"
 ORDER BY g.`name`ASC;
