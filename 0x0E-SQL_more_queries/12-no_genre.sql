-- Lists all shows in the database hbtn_0d_tvshows without a genre linked.
-- Records are ordered by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
       WHERE g.`genre_id` IS NULL
 ORDER BY s.`title`, g.`genre_id`;
