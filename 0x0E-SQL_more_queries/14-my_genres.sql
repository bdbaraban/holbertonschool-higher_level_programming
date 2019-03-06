-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- Records are ordered by ascending genre name.
SELECT g.`name`
  FROM `tv_genres` as g
       INNER JOIN `tv_show_genres` as s
       ON g.`id` = s.`genre_id`

       INNER JOIN `tv_shows` as t
       ON t.`id` = s.`show_id`
       WHERE t.`title` = "Dexter"
 ORDER BY g.`name`;
