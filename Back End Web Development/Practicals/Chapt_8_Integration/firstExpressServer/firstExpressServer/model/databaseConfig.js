var mysql = require('mysql2');

var dbconnect = {
getConnection: function() {
    var conn = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "T0530750Z",
    database: "furniture"
});
return conn;
}
};

module.exports = dbconnect