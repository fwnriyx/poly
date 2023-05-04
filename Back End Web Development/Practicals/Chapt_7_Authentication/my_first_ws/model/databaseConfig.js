var mysql = require('mysql2');
var dbconnect = {
    getConnection: function () {
        var conn = mysql.createConnection({
            host: "localhost",
            user: "root",
            password: "T0530750Z", // MUST change to your own password you use when installing MySQL
            database: "furniture",
            dateStrings: true
        });     
        return conn;
    }
};
module.exports = dbconnect
