var mysql = require('mysql');

var dbconnect = {
getConnection: function() {
    var conn = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "password", //"root",
    database: "furniture"
});
return conn;
}
};

module.exports = dbconnect