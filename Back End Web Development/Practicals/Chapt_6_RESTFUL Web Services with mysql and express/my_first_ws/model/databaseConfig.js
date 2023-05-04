var mysql = require('mysql2');
var dbconnect = {
    getConnection: function() {
        var conn = mysql.createConnection({
            host: "localhost",
            user: "root", // follow the spects documented in the writeup
            password: "T0530750Z", // ur own password when installing db or when creating
            database: "furniture", 
            dateStrings: true
        });
        return conn;
    }
};

module.exports = dbconnect