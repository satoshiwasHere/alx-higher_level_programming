-- script lists all Comedy shows in the database hbtn_0d_tvshows

SELECT t.`title`
  FROM `shows` AS t
       INNER JOIN `show_genres` AS s
       ON t.`id` = s.`show_id`

       INNER JOIN `genres` AS g
       ON g.`id` = s.`genre_id`
       WHERE g.`genre_name` = "Comedy"
 ORDER BY t.`title`;
