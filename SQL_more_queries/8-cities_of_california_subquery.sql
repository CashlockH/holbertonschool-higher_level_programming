-- cities of California
SELECT
  id,
  name
FROM
  cities
WHERE
  state_id IN (
    SELECT
      id
    FROM
      state
    WHERE
      name = 'California'
  )
ORDER BY
  id ASC;
