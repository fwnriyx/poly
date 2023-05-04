var db = require('./databaseConfig.js');

var config = require('../config.js');
var jwt = require('jsonwebtoken');

var userDB = {
    // // v1
    // loginUser: function (email,password, callback) {
    //     var conn = db.getConnection();
    //     conn.connect(function (err) {
    //         if (err) {
    //             console.log(err);
    //             return callback(err,null);
    //         }
    //         else {
    //             console.log("Connected!");
    //             var sql = 'select * from user where email=? and password=?';
    //             conn.query(sql, [email,password], function (err, result) {
    //                 conn.end();
    //                 if (err) {
    //                     console.log(err);
    //                     return callback(err,null);
    //                 } else {
    //                     var msg="{\"result\":\""+result.length+"\"}";                          
    //                     return callback(null, msg);
    //                 }
    //             });
    //         }
    //     });
    // },

loginUser: function (email,password, callback) {
        var conn = db.getConnection();
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err,null);
            } else {
                console.log("Connected!");
                var sql = 'select * from user where email=? and password=?';
                conn.query(sql, [email,password], function (err, result) {
                    conn.end();  
                    if (err) {
                        console.log(err);
                        return callback(err,null);  
                    } else {
                         //console.log(config.key);
                        var token = "";
                        if(result.length==1){
                            token = jwt.sign({userid:result[0].userid,role:result[0].role},config.key,{
                                expiresIn:86400//expires in 24 hrs
                            });
                        }
                        return callback(null,token);
            
                    }
                });            
            }
        });
    },
    


getUser: function (userid, callback) { // usually used by a single user to get own record
    var conn = db.getConnection();
    conn.connect(function (err) {
        if (err) {
            console.log(err);
            return callback(err, null);
        } else {
            // console.log("Connected!"); // NOT useful
            console.log("Connected to furniture db in user.js getUser function");
            // var sql = 'SELECT * FROM user WHERE userid = ?'; // use * with lots of care
            // var sql = `SELECT * FROM user WHERE userid = ${userid}`; // dangerous due to sql injection
            var sql = `SELECT userid, username, email, created_at FROM user WHERE userid = ?`;
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

getUsers: function (callback) { // usually used by admin 
    var conn = db.getConnection();
    conn.connect(function (err) {
        if (err) {
            console.log(err);
            return callback(err, null);
        } else {
            console.log("Connected to furniture db in user.js getUsers function");
            var sql = `SELECT userid, username, email, created_at FROM user`;
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
            console.log("Connected to furniture db in user.js addUser function");
            var sql = 'Insert into user(username, email, role, password, profile_pic_url) values(?,?,?,?,?)';

            conn.query(sql, [username, email, role, password, profile_pic_url], function (err, result) {
                conn.end();
                if (err) {
                    console.log(err);
                    return callback(err, null);
                } else {
                    // console.log(result.affectedRows);
                    // return callback(null, result.affectedRows);
                    console.log(result.insertId); // pretty popular for insert operation
                    return callback(null, result.insertId);
                }
            });
        }
    });
},

updateUser: function (email, password, userid, callback) { // usually used by a single user to get own record
    var conn = db.getConnection();
    conn.connect(function (err) {
        if (err) {
            console.log(err);
            return callback(err, null);
        } else {
            console.log("Connected to furniture db in user.js updateUser function");
            //The sql should be similar to var sql = 'Update user set email=?,password=? where userid=?';
            //your code
            var sql = 'Update user set email=?,password=? where userid=?';
            conn.query(sql, [email, password, userid], function (err, result) {
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

deleteUser: function (userid, callback) { // usually used by admin
    var conn = db.getConnection();
    conn.connect(function (err) {
        if (err) {
            console.log(err);
            return callback(err, null);
        } else {
            console.log("Connected to furniture db in user.js deleteUser function");
            var sql = 'DELETE FROM user WHERE userid=?';
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

module.exports = userDB

