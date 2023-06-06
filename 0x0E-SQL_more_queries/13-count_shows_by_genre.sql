-- Script that lists all genres from hbtn_0d_tvshows and,
-- displays the number of shows linked to each.
SELECT g.name AS genre,
	COUNT(show_genre.genre_id) AS number_of_shows
FROM show_genres
	INNER JOIN tv_genres
	ON show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;
