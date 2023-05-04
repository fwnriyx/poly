var db = require('./databaseConfig.js');
module.exports = {
    getUser: function (userid, callback) { // usually used by single user for own record
        var conn = db.getConnection();
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                console.log("Connected to furniture database in user.js getUser function");
                // var sql = 'SELECT * FROM user WHERE userid = ?'; // be careful using *
                // var sql = `SELECT 
                //                 userid, username, email, profile_pic_url, created_at 
                //            FROM 
                //                 user 
                //            WHERE 
                //                 userid = ${userid}`; // do NOT do this. Hackers will love you for this. Dont put it in the same line
                var sql = `SELECT 
                                userid, username, email, profile_pic_url, created_at 
                           FROM 
                                user 
                           WHERE 
                                userid = ?`;
                conn.query(sql, [userid], function (err, result) {
                    conn.end();
                    if (err) {
                        console.log(err);
                        return callback(err, null);
                    } else {
                        return callback(null, result);
                    }
                });
            }
        });
    },

    getUsers: function (callback) { //Usually used to get more records
        var conn = db.getConnection();
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                console.log("Connected to furniture database in user.js getUser function");
                var sql = `SELECT userid, username, email, profile_pic_url, created_at FROM user WHERE userid = ?`;
                conn.query(sql, function (err, result) {
                    conn.end();
                    if (err) {
                        console.log(err);
                        return callback(err, null);
                    } else {
                        return callback(null, result);
                    }
                });
            }
        });
    },

    addUser: function (username, email, role, password, profile_pic_url, callback) {
        var conn = db.getConnection();
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                console.log("Connected to furniture database in user.js updateUser function")
                var sql = 'UPDATE user set email = ?,password = ? WHERE userid = ?'
                conn.query(sql, [username, email, role, password, profile_pic_url], function (err, result) {
                    conn.end();
                    if (err) {
                        console.log(err);
                        return callback(err, null);
                    } else {
                        // console.log(result.affectedRows);
                        // return callback(null,result.affectedRows);
                        console.log(result.insertId)
                        return callback(null, result.insertId)
                    }
                });
            }
        });
    },
    updateUser: function (email, password, userid, callback) {
        var conn = db.getConnection();
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                console.log("Connected!");
                var sql = 'Insert into user(username,email,role,password, profile_pic_url) values(?,?,?,?,?)';
                conn.query(sql, [username, email, role, password, profile_pic_url], function (err, result) {
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

        //The sql should be similar to var sql = 'Update user set email=?,password=? //where userid=?';
        //your code 
    },

    deleteUser: function (userid, callback) { // usually used by admin 
        var conn = db.getConnection();
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                console.log("Connected to furniture database in user.js deleteUser function");
                // var sql = 'SELECT * FROM user WHERE userid = ?'; // be careful using *
                // var sql = `SELECT 
                //                 userid, username, email, profile_pic_url, created_at 
                //            FROM 
                //                 user 
                //            WHERE 
                //                 userid = ${userid}`; // do NOT do this. Hackers will love you for this. Dont put it in the same line
                var sql = 'Delete from user where userid = ?';
                conn.query(sql, [userid], function (err, result) {
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
    },
}

