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
    // Endpoint 8: POST /customers Add a new customer to the database (note: customer’s email address is unique)
    addCustomer: (address, address2, district, city_id, postal_code, phone, store_id, first_name, last_name, email, callback) => {
        var conn = db.getConnection();
        conn.connect((err) => {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                const sql = `INSERT INTO address (address, address2, district, city_id, postal_code, phone) VALUES (?, ?, ?, ?, ?, ?);
                             INSERT INTO customer(store_id, first_name, last_name, email, address_id) VALUES (?, ?, ?, ?, LAST_INSERT_ID())`;
                if (store_id != "" && first_name != "" && last_name != "" && email != "") {
                    conn.query(sql, [address, address2, district, city_id, postal_code, phone, store_id, first_name, last_name, email], function (err, result) {
                        if (err) {
                            console.log(err);   
                            return callback(err, result);
                        } else {
                            const finalMsg = { "customer_id": result[1].insertId };
                            return callback(null, finalMsg);
                        }
                    });
                } else {
                    var result = 0
                    return callback(null, result);
                }
            }
        });
    },
}