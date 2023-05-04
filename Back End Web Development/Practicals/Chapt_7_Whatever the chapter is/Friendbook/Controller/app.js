var express = require('express');
var app = express();
var actors = require('../model/user.js');

app.use(express.json());
app.use(express.urlencoded({ extended: false }))

// Endpoint 1: GET /actors/{actor_id} Return actor information of the given actor_id.

app.get('/actor/:actor_id', function (req, res) {
    var actor_id_str = req.params.actor_id; // use same variable name. use parseInt
    if (isNaN(actor_id_str)) {
        res.status(404).json({ message: `Invalid input. Please try again.` })
    } else {
        var actor_id = parseInt(actor_id_str);
        actors.getOneActor(actor_id, function (err, result) {
            if (!err) {
                res.status(200).json(result[0]);
            } else if (actor_id.length == 0) {
                res.status(204).json();
            } else {
                res.status(500).json({ message: `Internal server error` });
            }
        });
    }
});


// Endpoint 2: GET /actors Return the list of actors ordered by first_name, limited to 20 records offset 0 by default.
app.get('/actors', function (req, res) {
    var {limit, offset} = req.query;
        actors.getActors(limit, offset , function (err, result) {
            if (!err) {
                res.status(200).json(result);
            } else {
                res.status(500).json({ message: `Internal server error` });
            }
        });
    }
);



// Endpoint 3 POST /actors Add a new actor to the database (note: actors can have the same first_name and last_name)

app.post('/actors', function (req, res) {
    var { first_name, last_name } = req.body;
    if (first_name.length == 0 || last_name.length == 0) {
        res.status(400).json({ error_msg: 'missing data'});
    } else {
        actors.addActors(first_name, last_name, function (err, result) {
            if (!err) {
                res.status(200).json({ actor_id:`${result}`  }); // more common
            } else {
                res.status(500).json({ error_msg: 'Internal server error' });
            }
        });
    }
});

// Endpoint 4: PUT /actors/{actor_id} Update actor’s first name or last name or both.

app.put('/actors/:actor_id', function (req, res) {
    var actor_id = parseInt(req.params.actor_id); // use same variable name. use parseInt
    var { first_name, last_name } = req.body;
    if (isNaN(actor_id)) {
        res.status(404).json({ message: `Unacceptable record id` })
    } else if(first_name.length == 0 && last_name.length == 0) {
        res.status(400).json({ error_msg: 'missing data'});
    } else {
        actors.updateActor(first_name,last_name,actor_id, function (err) {
            if (!err) {
                res.status(200).json({success_msg: `record updated`});
            } else if (actor_id.length == 0) {
                res.sendStatus(204)
            } else {
                res.status(500).json({ error_msg: `Internal server error` });
            }
        });
    };
});

// Endpoint 5: DELETE /actors/{actor_id} Remove actor from database.
app.delete('/actors/:actor_id', function (req, res) {
    var actor_id = parseInt(req.params.actor_id); // use same variable name. use parseInt
    if (isNaN(actor_id)) {
        res.status(404).json({ message: `Unacceptable record id` })
    } else {
        actors.deleteActor(actor_id, function (err, result) {
            if (!err) {
                res.status(200).json({success_msg: `actor deleted`});
            } else {
                res.status(500).json({ error_msg: `Internal server error` });
            }
        });
    }
});


/* Endpoint 6: GET /film_categories/{category_id}/films Return the film_id, title, rating, release_year 
   and length of  all films belonging to a category.
*/

// Endpoint 7: GET /customer /{customer_id}/payment Return the payment detail of a customer between the provided period.

// Endpoint 8: POST /customers Add a new customer to the database (note: customer’s email address is unique)


module.exports = app


