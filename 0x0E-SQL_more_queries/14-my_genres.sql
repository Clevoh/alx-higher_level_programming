-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- Records are ordered by ascending order genre name.
SELECT n.`name`
  FROM `tv_genres` AS n
       INNER JOIN `tv_show_genres` AS s
       ON n.`id` = s.`genre_id`

       INNER JOIN `tv_shows` AS t
       ON t.`id` = s.`show_id`
       WHERE t.`title` = "Dexter"
 ORDER BY n.`name`;
