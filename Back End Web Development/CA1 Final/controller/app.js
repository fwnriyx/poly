var express = require('express');
var app = express();
var actors = require('../model/user.js');

app.use(express.json());
app.use(express.urlencoded({extended: false}))

// Endpoint 1   GET user/:userid empty Retrieve data of user with id <num>
app.get('/actor/:actor_id', function (req, res) {
    var actor_id = parseInt(req.params.actor_id); // use same variable name. use parseInt
    if (isNaN(actor_id)) {
        res.status(404).json({ message: `Invalid input. Please try again.` })
    } else {
        actors.getUser(actor_id, function (err, result) {
            if (!err) {
                res.status(200).json(result);
            } else {
                res.status(500).json({ message: `Internal server error` });
            }
        });
    }
});

// Endpoint 2  GET user empty Retrieve data of all users

// Endpoint 3	POST user  JSON String of user details	Insert new user record 
app.post('/actors', function (req, res) {
    var { first_name,last_name} = req.body;
     actors.addActors(first_name,last_name, function (err, result) {
        if (!err) {
            res.status(200).json({message: `New record with id <${result}> record inserted`}); // more common
        } else {
            res.status(500).json({ message: `Some error` });
        }
    });
});

// Endpoint 4	PUT user/:userid	 JSON String of updated user details	Update user with id <num> 

// Endpoint 5	DELETE /user/:userid empty	 Delete user with id <num>

module.exports = app
