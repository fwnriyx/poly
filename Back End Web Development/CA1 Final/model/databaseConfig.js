var mysql = require('mysql2');
var dbconnect = {
    getConnection: function() {
        var conn = mysql.createConnection({
            host: "localhost",
            user: "bed_dvd_root", // follow the specs documented in the writeup
            password: "pa$$woRD123", // ur own password when installing db or when creating
            database: "sakila", 
            dateStrings: true
        });
        return conn;
    }
};

module.exports = dbconnect