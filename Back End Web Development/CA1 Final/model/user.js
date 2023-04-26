var db = require('./databaseConfig.js');
module.exports = {
    getUser: function (actor_id, callback) { // usually used by single user for own record
        var conn = db.getConnection();
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                console.log("Connected to actors database in user.js getUser function");
                var sql = `SELECT 
                                actor_id, first_name, last_name 
                           FROM 
                                sakila.actor 
                           WHERE 
                                actor_id = ?`;
                conn.query(sql, [actor_id], function (err, result) {
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

    addActors: function (first_name, last_name, callback) {
        var conn = db.getConnection();
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                console.log("Connected to database in user.js updateUser function")
                var sql = `INSERT INTO actor
                                (first_name, last_name)
                            VALUES
                                (?, ?)`;
                conn.query(sql, [first_name, last_name], function (err, result) {
                    conn.end();
                    if (err) {
                        console.log(err);
                        return callback(err, null);
                    } else {
                        console.log(result.insertId)
                        return callback(null, result.insertId)
                    }
                });
            }
        });
    },
    updateUser: function (email, password, actor_id, callback) {
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
    },

    deleteUser: function (userid, callback) { // usually used by admin 
        var conn = db.getConnection();
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                console.log("Connected to furniture database in user.js deleteUser function");
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

