var mysql = require('mysql2');
var dbconnect = {
    getConnection: function() {
        var conn = mysql.createConnection({
            host: "localhost",
            port: 3306,
            user: "root", // follow the specs documented in the writeup
            password: "T0530750Z", // ur own password when installing db or when creating
            database: "friendbook", 
            dateStrings: true
        });
        return conn;
    }
};

module.exports = dbconnect