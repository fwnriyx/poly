const db = require("./databaseConfig");
module.exports = {
    getUserPosts: function (userID, callback) {
        var dbConn = db.getConnection();
        dbConn.connect(function (err) {
            if (err) {//database connection gt issue!
                console.log(err);
                return callback(err, null);
            } else {
                const findPostsByIDQuery = // more readable sql output
                    `SELECT
                        text_body,
                        created_at
                    FROM
                        post
                    WHERE
                        fk_poster_id = ?;`;
                dbConn.query(findPostsByIDQuery, [userID], (error, results) => {
                    dbConn.end();
                    if (error) {
                        return callback(error, null);
                    } else if (results.length == 0) {
                        return callback(null, null);
                    } else {
                        return callback(null, results); // results has no square brackets
                    }
                });
            }
        });
    },

    insertUserPost: function (userID, postTextBody, callback) {
        var dbConn = db.getConnection();
        dbConn.connect(function (err) {
            if (err) {//database connection gt issue!
                console.log(err);
                return callback(err, null);
            } else {
                const insertPostByUserQuery = // more readable sql output
                    `INSERT INTO
                        post (fk_poster_id, text_body)
                    VALUES (?,?);`;
                dbConn.query(insertPostByUserQuery, [userID, postTextBody], (error, results) => {
                    dbConn.end();
                    if (error) {
                        return callback(error, null);
                    } else if (results.affectedRows == 0) {
                        return callback(null, null);
                    } else {
                        return callback(null, results);
                    }
                });
            }
        });
    },

    getPostByID: function (postID, callback) {
        var dbConn = db.getConnection();
        dbConn.connect(function (err) {
            if (err) {//database connection gt issue!
                console.log(err);
                return callback(err, null);
            } else {
                const findPostsByIDQuery = // more readable sql output
                    `SELECT
                        text_body,
                        created_at
                    FROM
                        post
                    WHERE
                        id = ?;`;
                dbConn.query(findPostsByIDQuery, [postID], (error, results) => {
                    dbConn.end();
                    if (error) {
                        return callback(error, null);
                    } else if (results.length == 0) {
                        return callback(null, null);
                    } else {
                        return callback(null, results); // results has no square brackets
                    }
                });
            }
        });
    }

}