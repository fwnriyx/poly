//P2222811: Muhammad Fitri Amir bin Abdullah DAAA/FT/1B/06

var db = require('./databaseConfig.js');
module.exports = {
    //Endpoint 3 POST /actors Add a new actor to the database (note: actors can have the same first_name and last_name)
    addActors: function (first_name, last_name, callback) {
        var conn = db.getConnection();
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                console.log("Connected to database in user.js addActors function")
                var sql = `INSERT INTO actor
                                (first_name, last_name)
                            VALUES
                                (?, ?)`;
                conn.query(sql, [first_name, last_name], function (err, result) {
                    conn.end();
                    if (err) {
                        console.log(err);
                        return callback(err, null);
                    } else {
                        console.log(result.insertId)
                        return callback(null, result.insertId)
                    }
                });
            }
        });
    },
    //Endpoint 4: PUT /actors/{actor_id} Update actor’s first name or last name or both.
    updateActor: function (actor_id, first_name, last_name, callback) {
        var conn = db.getConnection();
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                const getUserQuery = `SELECT first_name, last_name FROM actor WHERE actor_id = ?`;
                var first_name1 = first_name;
                var last_name1 = last_name; 
                conn.query(getUserQuery, [actor_id], (error, result) => {
                    if (error) {
                        return callback(error, null);
                    } else if(result.length == 0){
                        return callback("No such user", null);
                    } else {
                        if (first_name1 == "") {first_name1 = result[0].first_name};
                        if (last_name1 == "") {last_name1 = result[0].last_name};
                        const editUserQuery = `UPDATE actor SET first_name = ?, last_name = ? WHERE actor_id = ?`;
                        conn.query(editUserQuery, [first_name1, last_name1, actor_id], (error, result) => {
                            conn.end();
                            if (error) {
                                return callback(error, null);
                            } else {
                                return callback(null, result);
                            }
                        });
                    }
                });

            }
        });
    },
    //Endpoint 5: DELETE /actors/{actor_id} Remove actor from database.
    deleteActor: function (actor_id, callback) {
        var conn = db.getConnection();
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                console.log("Connected to furniture database in user.js deleteActor function");
                var sql = `DELETE FROM actor WHERE actor_id = ?;`
                conn.query(sql, [actor_id], function (err, result) {
                    conn.end();
                    if (err) {
                        console.log(err);
                        return callback(err, null);
                    } else {
                        return callback(null, result.affectedRows);
                    }
                });
            }
        });
    }
}


