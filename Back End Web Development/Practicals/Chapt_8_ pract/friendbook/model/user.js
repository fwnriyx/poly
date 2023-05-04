// we can rename connection as db or anything we choose.
const db = require("./databaseConfig");

// const User = {
// };
// module.exports = User;

module.exports = {

    // Login function - change function name from verify to loginUser
    loginUser: function (username, password, callback) { // copied from practical7 notes
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
    
    // user.findByID(id, callback)
    findByID: function(userID, callback) {
        var dbConn = db.getConnection();
        dbConn.connect(function (err) {
            if (err) {//database connection gt issue!
                console.log(err);
                return callback(err, null);
            } else {
            // We can use "?" as placeholder for user provided data.
            // The userID is passed in through the second parameter of the query  
            // method.
            // This is done instead of using string templates to prevent SQL 
            // injections.
            // https://github.com/mysqljs/mysql#escaping-query-values
                const findUserByIDQuery = "SELECT * FROM user WHERE id = ?;";
                dbConn.query(findUserByIDQuery, [userID], (error, results) => {
                    dbConn.end();
                    if (error) {
                        return callback(error, null);
                    } else if (results.length === 0) {
                        callback(null, null);
                        return;
                    } else {
                        // console.log(results);
                        let {password, date_of_birth, id, ...theRest} = results[0];
                        return callback(null, theRest);
                        // return callback(null, results[0]);
                    }
                });
            }
        });
    },
    
    // user.findAll(callback)
    findAll: function(callback) {
        var dbConn = db.getConnection();
        dbConn.connect(function (err) {
            if (err) {//database connection gt issue!
                console.log(err);
                return callback(err, null);
            } else {
                const findAllUsersQuery = "SELECT full_name, bio FROM user ORDER BY full_name;";
                dbConn.query(findAllUsersQuery, (error, results) => {
                    if (error) {
                        return callback(error, null);
                    };
                    return callback(null, results);
                });
            }
        });
    },
      
    // user.insert(user, callback)
    insert: function(user, callback) {
        var conn = db.getConnection();
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err,null);
            } else {
                console.log("Connected to database in user.js insert function");
                const { full_name, username, bio, date_of_birth} = user;
                var sql = 'INSERT INTO user (full_name, username, bio, date_of_birth) VALUES (?,?,?,?)';
                conn.query(sql, [full_name, username, bio, date_of_birth], function (err, result) {
                    conn.end();
                    if (err) {
                        console.log(err);
                        return callback(err, null);
                    } else {
                        // console.log(result.affectedRows);
                        // return callback(null, result.affectedRows);
                        console.log(result.insertId); // commonly asked for in most implementation
                        return callback(null, result.insertId);
                    }
                });
            }
        });
    },

    // user.edit(userID, user, callback)
    edit: function(userID, user, callback) {
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
                        var {full_name, username, bio, date_of_birth} = user;
                        console.log(full_name, username, bio, date_of_birth);
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
                            };
                            return callback(null, results);
                        });
                    }
                });

            }
        });
    },

    // user.delete(userID, callback)
    delete: function(userID, callback) {
        var conn = db.getConnection();
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err,null);
            } else {    
                console.log("Connected to database in user.js delete function");      
                var sql = 'Delete from user where id = ?';
                conn.query(sql, [userID], function (err, result) {
                    conn.end();
                    if (err) {
                        console.log(err);
                        return callback(err, null);
                    } else {
                        return callback(null, result.affectedRows);
                    }
                });
            }        
        }); 
    }
}
