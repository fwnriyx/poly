//P2222811: Muhammad Fitri Amir bin Abdullah DAAA/FT/1B/06

const config = require('../config.js'); 
const jwt = require('jsonwebtoken');

var db = require('./databaseConfig.js');
module.exports = {
    loginUser: function (email, password, callback) {
        var dbConn = db.getConnection();
        dbConn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                const query = "SELECT staff_id FROM staff WHERE email = ? AND password = ?";
                dbConn.query(query, [email, password], (error, result) => {
                    if (error) {
                        callback(error, null);
                        return;
                    } else if (result.length === 0) {
                        return callback(new Error("Invalid email or password"), null);
                    } else {
                        var token = "";
                        const payload = {staff_id:result[0].staff_id,token: token }
                        token = jwt.sign(payload, config.key, {
                            expiresIn: 86400 //valid for 24 hours
                        })
                        console.log('Login.js successful')
                        callback(null, token, result)
                    }
                    dbConn.end();
                });
            }
        });
    }
}