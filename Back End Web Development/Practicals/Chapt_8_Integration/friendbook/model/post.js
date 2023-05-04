var db = require('./databaseConfig.js');
module.exports = {
    // addFriend(userIDOne, userIDTwo, callback)
    // removeFriend(userIDOne, userIDTwo, callback)

    // showFriends(userID, callback)
    getUserPosts: function (userID, callback) {
        var dbConn = db.getConnection();
        dbConn.connect(function (err) {
            if (err) {//database connection gt issue!
                console.log(err);
                return callback(err, null);
            } else {
                const sql = `
                    SELECT
                        text_body,
                        created_at
                    FROM
                        post
                    WHERE
                        fk_poster_id = ?;`;
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