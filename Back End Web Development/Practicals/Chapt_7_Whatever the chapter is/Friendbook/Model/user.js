var db = require('./databaseConfig.js');
module.exports = {
    //findByID(id, callback)
    findByID: function (userID, callback) {
        var dbConn = db.getConnection();
        dbConn.connect(function (err) {

            if (err) {//database connection gt issue!

                console.log(err);
                return callback(err, null);
            } else {
                // We can use "?" as placeholder for user provided data.
                // The userID is passed in through the second parameter of the query  
                // method.
                // This is done instead of using string templates to prevent SQL 
                // injections.
                // https://github.com/mysqljs/mysql#escaping-query-values

                const findUserByIDQuery = "SELECT * FROM user WHERE id = ?;"; // be mindful on use of *
                dbConn.query(findUserByIDQuery, [userID], (error, results) => {
                    dbConn.end();
                    if (error) {
                        return callback(error, null);
                    } else if (results.length == 0) {
                        return callback(null, null);
                    } else {
                        // console.log(results);
                        return callback(null, results[0]);
                    }
                });
            }
        });
    },

    //findAll(callback)
    findAll: function (callback) {
        var dbConn = db.getConnection();
        dbConn.connect(function (err) {
            if (err) {//database connection gt issue!
                console.log(err);
                return callback(err, null);
            } else {
                const findAllUsersQuery = "SELECT * FROM user;";
                dbConn.query(findAllUsersQuery, (error, results) => {
                    if (error) {
                        return callback(error, null);
                    };
                    return callback(null, results);
                });
            }

            //insert(user, callback)
            //edit(userID, user, callback)
            //delete(userID, callback)
        });
    }
}
