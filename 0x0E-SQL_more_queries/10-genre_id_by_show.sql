-- Import the database dump from hbtn_0d_tvshows to your MySQL server:
-- Script lists all shows contained in hbtn_0d_tvshows

SELECT show.`title`, gnr.`genre_id` FROM `tv_shows` AS show
        INNER JOIN `tv_show_genres` AS gnr
	ON show.`id` = gnr.`show_id'
 ORDER BY show.`title`, gnr.`genre_id`;
