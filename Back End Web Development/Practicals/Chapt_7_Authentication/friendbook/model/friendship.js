var db = require('./databaseConfig.js');
module.exports = {
    // addFriend(userIDOne, userIDTwo, callback)
    // removeFriend(userIDOne, userIDTwo, callback)

    // showFriends(userID, callback)
    showFriends: function (userID, callback) {
        var dbConn = db.getConnection();
        dbConn.connect(function (err) {
            if (err) {//database connection gt issue!
                console.log(err);
                return callback(err, null);
            } else {
                // const sql = `
                //     SELECT
                //         u.full_name AS MyFriends
                //     FROM
                //         user u,
                //         friendship f
                //     WHERE
                //         u.id = f.fk_friend_two_id
                //             AND
                //         f.fk_friend_one_id = ?;`;
                const sql = `
                    SELECT
                        GROUP_CONCAT(u.full_name SEPARATOR ", ") AS MyFriends
                    FROM
                        user u,
                        friendship f
                    WHERE
                        u.id = f.fk_friend_two_id
                            AND
                        f.fk_friend_one_id = ?;`;
                dbConn.query(sql, [userID], (error, results) => {
                    dbConn.end();
                    if (error) {
                        callback(error, null);
                    } else if (results.length == 0) {
                        callback(null, null);
                    } else {
                        callback(null, results);
                    }
                });
            } 
        });
    }

}