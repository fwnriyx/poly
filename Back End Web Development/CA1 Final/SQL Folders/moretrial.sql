-- SELECT  * FROM USER; -- try to avoid use of * where security/privacy is important
-- SELECT id, full_name, username FROM user;
-- SELECT full_name, id, username FROM user; 
-- SELECT full_name, id, username FROM user ORDER BY full_name ASC LIMIT 3; -- my sql is case sensitive. using workbench to our adv.
-- SELECT full_name, id, username AS "Login Name" FROM user ORDER BY full_name DESC LIMIT 3;
-- SELECT full_name, id, username AS "Login Name" FROM user where id = 4;
-- SELECT full_name, id, username AS "Login Name" FROM user WHERE full_name LIKE "Ron%";
-- SELECT full_name, id, username AS "Login Name" FROM user WHERE full_name LIKE "o%";
-- SELECT * FROM user WHERE id = 999;

-- INSERT INTO post (fk_poster_id, text_body) VALUES (4, 'I love going to the beach!');
-- INSERT INTO post (fk_poster_id, text_body) VALUES (3, 'I love going to the beach too!');
-- SELECT * FROM post WHERE fk_poster_id = 3;

-- The following sql will generate an error as user 999 does not exist.
-- INSERT INTO post(fk_poster_id, text_body) VALUES (999, 'I love going to the beach but');

-- UPDATE user
-- SET
--     full_name = 'Dexter Ng',
--     username = 'dexter_ng'
-- WHERE id = 2;
-- SELECT * FROM user WHERE id = 2;

-- DELETE FROM post WHERE id = 2;
-- SELECT * FROM post;

-- INSERT INTO likes
-- (fk_user_id, fk_post_id)
-- VALUES
-- (4, 3);
-- SELECT * FROM likes ORDER BY id DESC LIMIT 3;

-- INSERT INTO likes
-- (fk_user_id, fk_post_id)
-- VALUES
-- (4, 6),
-- (4, 7);
-- SELECT * FROM likes ORDER BY id DESC LIMIT 3;

-- INSERT INTO friendship
-- (fk_friend_one_id, fk_friend_two_id)
-- VALUES
-- (2, 3),
-- (3, 2);
-- SELECT * FROM friendship ORDER BY id DESC LIMIT 4;

-- SELECT fk_friend_two_id
-- FROM friendship
-- WHERE fk_friend_one_id = 2;

SELECT 
	u. full_name AS "My Friends"
FROM 
	friendship f, 
    user u
WHERE 
	f.fk_friend_one_id = 2
		AND
	u.id = f.fk_friend_two_id;