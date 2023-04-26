//P2222811: Muhammad Fitri Amir bin Abdullah DAAA/FT/1B/06

const express = require('express');
var db = require('./databaseConfig.js');
module.exports = {
    showFilm: (film_id, callback) => { //for endpoint 8: get row from product table by primary key (productid)
        var conn = db.getConnection();
        conn.connect(function(err) {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                console.log("Connected to MySQL from product.js, executing product.showByID");
                var sqlQuery =
                    `SELECT actor.first_name, actor.last_name, film.title, category.name,film.release_year,film.description,film.rating
                    FROM film 
                    INNER JOIN film_category ON film.film_id = film_category.film_id
                    INNER JOIN category ON film_category.category_id = category.category_id
                    inner join film_actor on film_actor.film_id = film.film_id
                    inner join actor on film_actor.actor_id = actor.actor_id
                    WHERE film.film_id = ?`
                
                conn.query(sqlQuery, [film_id], function(err, result) {
                    if (err) {
                        return callback(err, null);
                    } else {
                        console.log(result)
                        return callback(null, result);
                    }
                });
            }
        });
    },

    search: (films, callback) => { //search film by title/category/rental_rate
        var conn = db.getConnection();

        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                console.log("GG")
                title = films.title;
                category = films.category;
                rental_rate = films.rental_rate;
                rating = films.rating;
                film_id = films.film_id;
                // console.log(films);
                if (category == 'Select Category') {
                    if (title != '' && rental_rate != '') {
                        console.log("Title + rental rate")
                        var sqlQuery =
                            `SELECT film.title AS title , category.name AS category, film.rental_rate AS rental_rate, film.film_id AS film_id, film.rating AS rating, film.release_year
                                FROM film 
                                INNER JOIN film_category ON film.film_id = film_category.film_id
                                INNER JOIN category ON film_category.category_id = category.category_id
                                WHERE film.title LIKE ? AND category.name = "New"
                                AND film.rental_rate <= ? ORDER BY film.release_year;`;

                        conn.query(sqlQuery, [`%${title}%`, rental_rate], function (err, result) {
                            conn.end();
                            if (err) {
                                return callback(err, null);
                            } else {
                                return callback(null, result);
                            }
                        });
                    }else if (title == '' && rental_rate != ''){
                        console.log("No title + rental rate")
                        var sqlQuery =
                            `SELECT film.title AS title , category.name AS category, film.rental_rate AS rental_rate, film.film_id AS film_id, film.rating AS rating, film.release_year
                             FROM film 
                             INNER JOIN film_category ON film.film_id = film_category.film_id
                             INNER JOIN category ON film_category.category_id = category.category_id
                             WHERE category.name = "New"
                             AND film.rental_rate <= ? ORDER BY film.release_year;`;

                        conn.query(sqlQuery, [rental_rate], function (err, result) {
                            conn.end();
                            if (err) {
                                return callback(err, null);
                            } else {
                                return callback(null, result);
                            }
                        });
                    }else if(rental_rate == '' && title != ''){
                        console.log("No title + rental rate")
                        var sqlQuery =
                            `SELECT film.title AS title , category.name AS category, film.rental_rate AS rental_rate, film.film_id AS film_id, film.rating AS rating, film.release_year
                             FROM film 
                             INNER JOIN film_category ON film.film_id = film_category.film_id
                             INNER JOIN category ON film_category.category_id = category.category_id
                             WHERE film.title LIKE ? ORDER BY film.release_year;`;
                        conn.query(sqlQuery, [`%${title}%`], function (err, result) {
                            conn.end();
                            if (err) {
                                return callback(err, null);
                            } else {
                                return callback(null, result);
                            }
                        });
                    } else{
                        console.log("Default Category")
                        var sqlQuery =
                            `SELECT film.title AS title , category.name AS category, film.rental_rate AS rental_rate, film.film_id AS film_id, film.rating AS rating, film.release_year
                             FROM film 
                             INNER JOIN film_category ON film.film_id = film_category.film_id
                             INNER JOIN category ON film_category.category_id = category.category_id
                             WHERE category.name = "New" ORDER BY film.release_year;`;

                        conn.query(sqlQuery, [`%${title}%`, rental_rate], function (err, result) {
                            conn.end();
                            if (err) {
                                return callback(err, null);
                            } else {
                                return callback(null, result);
                            }
                        });
                    }
                } else if (title != '' && rental_rate != '') {
                        console.log("title!")
                        var sqlQuery =
                            `SELECT film.title AS title , category.name AS category, film.rental_rate AS rental_rate, film.film_id AS film_id, film.rating AS rating, film.release_year
                             FROM film 
                             INNER JOIN film_category ON film.film_id = film_category.film_id
                             INNER JOIN category ON film_category.category_id = category.category_id
                             WHERE (film.title LIKE ? AND category.name = ?)
                             AND film.rental_rate <= ?;`;

                        conn.query(sqlQuery, [`%${title}%`, `${category}`, rental_rate], function (err, result) {
                            conn.end();
                            if (err) {
                                return callback(err, null);
                            } else {
                                return callback(null, result);
                            }
                        });
                } else if (title == '' && rental_rate == '') {
                    console.log("no title/rate dog")
                    var sqlQuery =
                        `SELECT film.title AS title , category.name AS category, film.rental_rate AS rental_rate, film.film_id AS film_id, film.rating AS rating, film.release_year
                        FROM film 
                        INNER JOIN film_category ON film.film_id = film_category.film_id
                        INNER JOIN category ON film_category.category_id = category.category_id
                        WHERE category.name = ?;`;
                    conn.query(sqlQuery, [`${category}`], function (err, result) {
                        console.log(category, rental_rate)
                        conn.end();
                        if (err) {
                            return callback(err, null);
                        } else {
                            return callback(null, result);
                        }
                    });
                } else if (title != '' && rental_rate == ''){
                    console.log("title no rate")
                        var sqlQuery =
                            `SELECT film.title AS title , category.name AS category, film.rental_rate AS rental_rate, film.film_id AS film_id, film.rating AS rating, film.release_year                                                             
                             FROM film 
                             INNER JOIN film_category ON film.film_id = film_category.film_id
                             INNER JOIN category ON film_category.category_id = category.category_id
                             WHERE (film.title LIKE ? AND category.name = ?);`;

                        conn.query(sqlQuery, [`%${title}%`, `${category}`], function (err, result) {
                            conn.end();
                            if (err) {
                                return callback(err, null);
                            } else {
                                return callback(null, result);
                            }
                        });
                } else if (title == '' && rental_rate != ''){
                    console.log("title!")
                        var sqlQuery =
                            `SELECT film.title AS title , category.name AS category, film.rental_rate AS rental_rate, film.film_id AS film_id, film.rating AS rating, film.release_year
                             FROM film 
                             INNER JOIN film_category ON film.film_id = film_category.film_id
                             INNER JOIN category ON film_category.category_id = category.category_id
                             WHERE category.name = ? AND film.rental_rate <= ?;`;
                        conn.query(sqlQuery, [`${category}`, rental_rate], function (err, result) {
                            conn.end();
                            if (err) {
                                return callback(err, null);
                            } else {
                                return callback(null, result);
                            }
                        });
                }
            }
        });
    },
    category: (callback) => { //for endpoint 8: get row from product table by primary key (productid)
        var conn = db.getConnection();
        conn.connect(function(err) {
            if (err) {
                console.log(err);
                return callback(err, null);
            } else {
                var sqlQuery =
                    `SELECT name from category`
                conn.query(sqlQuery, function(err, result) {
                    if (err) {
                        return callback(err, null);
                    } else {
                        console.log(result)
    
                        return callback(null, result);
                    }
                });
            }
        });
    }

}