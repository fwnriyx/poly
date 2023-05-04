const mysql = require("mysql");
var dbconnect = {
    getConnection: function () {
  
      var conn = mysql.createConnection({
        host: 'localhost',
        port: 3306,
        user: 'root',
        password: 'password', //your own password
        database: 'friendbook',
        dateStrings: true
      });
  
      return conn;
    }
  };
  
  // put this at the end of the file
  module.exports = dbconnect;
  