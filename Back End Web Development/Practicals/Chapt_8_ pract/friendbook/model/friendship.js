const db = require("./databaseConfig");
module.exports = {

    // addFriend(userIDOne, userIDTwo, callback)
    addFriend: function(userIDOne, userIDTwo, callback) {
        var conn = db.getConnection();
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err,null);
            } else {
                console.log("Connected to database in friendship.js addFriend function");
                var sql = 'INSERT INTO friendship (fk_friend_one_id, fk_friend_two_id) VALUES (?,?), (?,?);';
                conn.query(sql, [userIDOne, userIDTwo, userIDTwo, userIDOne], function (err, result) {
                    conn.end();
                    if (err) {
                        console.log(err);
                        return callback(err, null);
                    } else {
                        console.log(result.affectedRows);
                        return callback(null, result.affectedRows);
                    }
                });
            }
        });
    },

    // removeFriend(userIDOne, userIDTwo, callback)

    // showFriends(userID, callback)
    showFriends: function (userID, callback) {
        var dbConn = db.getConnection();
        dbConn.connect(function (err) {
            if (err) {//database connection gt issue!
                console.log(err);
                return callback(err, null);
            } else {
                const findFriendsByIDQuery = `
                    SELECT
                        u.id,
                        u.full_name
                    FROM
                        user u,
                        friendship f
                    WHERE
                        u.id = f.fk_friend_two_id
                        AND
                        f.fk_friend_one_id = ?
                    ORDER BY
                        u.full_name;`;
                // const findFriendsByIDQuery = `
                // SELECT
                //     GROUP_CONCAT(u.full_name SEPARATOR ", ") AS "MyFriends"
                // FROM
                //     user u,
                //     friendship f
                // WHERE
                //     u.id = f.fk_friend_two_id
                //     AND
                //     f.fk_friend_one_id = ?;`;
                dbConn.query(findFriendsByIDQuery, [userID], (error, results) => {
                    dbConn.end();
                    if (error) {
                        callback(error, null);
                    } else if (results.length === 0) {
                        callback(null, null);
                    } else {
                        callback(null, results);
                    }
                });
            }
        });
    }

}

