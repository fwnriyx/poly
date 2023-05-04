const mysql = require("mysql2");
var dbconnect = {
    getConnection: function () {
  
      var conn = mysql.createConnection({
        host: 'localhost',
        port: 3306,
        user: 'root',
        password: 'T0530750Z', //your own password
        database: 'friendbook',
        dateStrings: true
      });
  
      return conn;
    }
  };
  
  // put this at the end of the file
  module.exports = dbconnect;
  