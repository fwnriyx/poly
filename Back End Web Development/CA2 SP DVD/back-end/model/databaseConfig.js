var mysql = require('mysql2');
var dbconnect = {
    getConnection: function() {
        var conn = mysql.createConnection({
            host: "localhost",
            port: 3306,
            user: "bed_dvd_root", // follow the specs documented in the writeup
            password: "pa$$woRD123", // ur own password when installing db or when creating
            database: "bed_dvd_db", 
            dateStrings: true,
            multipleStatements: true
        });
        return conn;
    }
};

module.exports = dbconnect