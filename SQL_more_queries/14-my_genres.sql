-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT DISTINCT
  tv_genres.name
FROM
  tv_genres
INNER JOIN
  tv_show_genres
ON
  tv_show_genres.genre_id = tv_genres.id
WHERE
  tv_show_genres.show_id = (
    SELECT
      id
    FROM
      tv_shows
    WHERE
      title = 'Dexter'
  );
