-- script lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS ts
       INNER JOIN `tv_show_ratings` AS sr
       ON ts.`id` = sr.`show_id`
 GROUP BY
`title`
 ORDER BY 
`rating` DESC
