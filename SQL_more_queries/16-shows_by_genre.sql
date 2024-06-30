SELECT
  tv_shows.title,
  tv_genres.name
FROM
  tv_shows
LEFT JOIN
  (tv_show_genres INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id)
ON
  tv_show_genres.show_id = tv_shows.id
ORDER BY
  tv_shows.title ASC;
