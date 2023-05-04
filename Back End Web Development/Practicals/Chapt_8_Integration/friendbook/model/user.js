// we can rename connection as db or anything we choose.
const db = require("./databaseConfig");

// const User = {
// };
// module.exports = User;

module.exports = {
    loginUser: function (username, password, callback) { //copied from pract 7 notes
        var dbConn = db.getConnection();
        dbConn.connect(function (err) {
            if (err) {//database connection gt issue!
                console.log(err);
                return callback(err, null);
            } else {
                const query = "SELECT * FROM user WHERE username=? AND password=?";
                dbConn.query(query, [username, password], (error, results) => {
                    if (error) {
                        callback(error, null);
                        return;
                    } else if (results.length === 0) {
                        return callback(null, null);
                    } else {
                        const user = results[0];
                        return callback(null, user);
                    }
                });
            }
        });
    },


    // findByID(id, callback)
    findByID: function (userID, callback) {
        var dbConn = db.getConnection();
        dbConn.connect(function (err) {
            if (err) {//database connection gt issue!
                console.log(err);
                return callback(err, null);
            } else {
                // We can use "?" as placeholder for user provided data.
                // The userID is passed in through the second parameter of the query method.
                // This is done instead of using string templates to prevent SQL injections.
                // https://github.com/mysqljs/mysql#escaping-query-values
                const findUserByIDQuery = "SELECT * FROM user WHERE id = ?;"; // be mindful on use of *
                dbConn.query(findUserByIDQuery, [userID], (error, results) => {
                    dbConn.end();
                    if (error) {
                        return callback(error, null);
                    } else if (results.length == 0) {
                        return callback(null, null);
                    } else {
                        // console.log(results);
                        let{password, date_of_birth, ...theRest} = results[0];
                        return callback(null, theRest);
                    }
                });
            }
        });
    },

    // findAll(callback)
    findAll: function (callback) {
        var dbConn = db.getConnection();
        dbConn.connect(function (err) {
            if (err) {//database connection gt issue!
                console.log(err);
                return callback(err, null);
            } else {
                // const findAllUsersQuery = "SELECT * FROM user;"; // mindful on use of *
                const findAllUsersQuery = "SELECT full_name, bio FROM user;"; // mindful on use of *
                dbConn.query(findAllUsersQuery, (error, results) => {
                    if (error) {
                        return callback(error, null);
                    } else if (results.length == 0) {
                        return callback(null, null);
                    } else {
                        return callback(null, results);
                    }
                });
            }
        });
    },

    // insert(user, callback)
    insert: function (newUser, callback) {
        var conn = db.getConnection();
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                console.log("Connected to friendbook database in user.js insert function");
                const { full_name, username, bio, date_of_birth } = newUser;
                var sql = 'INSERT INTO user(full_name, username, bio, date_of_birth) VALUES(?,?,?,?)';
                conn.query(sql, [full_name, username, bio, date_of_birth], function (err, newUserResult) {
                    if (err) {
                        console.log(err);
                        return callback(err, null);
                    } else {
                        sql = `SELECT created_at FROM user WHERE id = ?;`;
                        conn.query(sql, [newUserResult.insertId], function (err, result) {
                            conn.end();
                            if (err) {
                                console.log(err);
                                return callback(err, null);
                            } else {
                                return callback(null, { newRecordId: newUserResult.insertId, created_at: result[0].created_at });
                            }
                        });
                    }
                });
            }
        });
    },

    // edit(userID, user, callback)
    edit: function (userID, newUserDetails, callback) { // Version 2
        var dbConn = db.getConnection();
        dbConn.connect(function (err) {
            if (err) {//database connection gt issue!
                console.log(err);
                return callback(err, null);
            } else {
                const getUserQuery =
                    `SELECT full_name, username, bio, date_of_birth FROM user WHERE id = ?`;
                dbConn.query(getUserQuery, [userID], (error, results) => {
                    if (error) {
                        return callback(error, null);
                    } else {
                        var { full_name, username, bio, date_of_birth } = newUserDetails;
                        if (full_name == undefined) full_name = results[0].full_name;
                        if (username == undefined) username = results[0].username;
                        if (bio == undefined) bio = results[0].bio;
                        if (date_of_birth == undefined) date_of_birth = results[0].date_of_birth;
                        const editUserQuery =
                            `UPDATE user SET full_name = ?, username = ?, bio = ?, date_of_birth = ? WHERE id = ?`;
                        dbConn.query(editUserQuery, [full_name, username, bio, date_of_birth, userID], (error, results) => {
                            dbConn.end();
                            if (error) {
                                return callback(error, null);
                            } else {
                                return callback(null, results.affectedRows);
                            }
                        });
                    }
                });

            }
        });
    },

    // delete(userID, callback)
    delete: function (userID, callback) { // usually used by admin
        var conn = db.getConnection();
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                console.log("Connected to friendbook database in user.js delete function");
                var sql = 'Delete from user where userid = ?';
                conn.query(sql, [userID], function (err, result) {
                    conn.end();
                    if (err) {
                        return callback(err, null);
                    } else if (result.affectedRows == 0) {
                        return callback(null, null);
                    } else {
                        return callback(null, result.affectedRows);
                    }
                });
            }
        });
    }
}
