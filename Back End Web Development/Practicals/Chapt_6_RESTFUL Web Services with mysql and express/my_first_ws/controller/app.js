var express = require('express');
var app = express();
var user = require('../model/user.js');

// var bodyParser = require('body-parser');
// var urlencodedParser = bodyParser.urlencoded({ extended: false });
// app.use(bodyParser.json());// parse application/json
// app.use(urlencodedParser); // parse application/x-www-form-urlencoded
app.use(express.json());
app.use(express.urlencoded({extended: false}))

// Endpoint 1   GET user/:userid	 empty	 Retrieve data of user with id <num>
app.get('/user/:userid', function (req, res) {
    var userid = parseInt(req.params.userid); // use same variable name. use parseInt
    if (isNaN(userid)) {
        res.status(404).json({ message: `Unacceptable record id` })
    } else {
        user.getUser(userid, function (err, result) {
            if (!err) {
                res.status(200).json(result);
            } else {
                res.status(500).json({ message: `Some error` });
            }
        });
    }
});

// Endpoint 2	GET user empty	 Retrieve data of all users
app.get('/user', function (req, res) {
    user.getUsers(function (err, result) {
        if (!err) {
            res.status(200).json(result);
        } else {
            res.status(500).json({ message: `Some error` });
        }
    });
});

// Endpoint 3	POST user		     JSON String of user details	Insert new user record 
app.post('/user/:userid', function (req, res) {
    var { username, email, role, password, profile_pic_url } = req.body;
     user.addUser(username, email, role, password, profile_pic_url, function (err, result) {
    // user.addUser(req.body, function (err, result) {
        if (!err) {
            // res.status(200).json({message: `${result} record inserted`}); // not common
            res.status(200).json({message: `New record with id <${result}> record inserted`}); // more common
        } else {
            res.status(500).json({ message: `Some error` });
        }
    });
});

// Endpoint 4	PUT user/:userid	 JSON String of updated user details	Update user with id <num> 
app.put('/user/:userid', function (req, res) {
    var userid = parseInt(req.params.userid); // use same variable name. use parseInt
    var { email, password } = req.body;
    if (isNaN(userid)) {
        res.status(404).json({ message: `Unacceptable record id` })
    } else {
        user.updateUser(email, password, userid, function (err, result) {
            if (!err) {
                res.status(200).json({message: `${result} record updated!`});
            } else {
                res.status(500).json({ message: `Some error` });
            }
        });
    }
});

// Endpoint 5	DELETE /user/:userid empty	 Delete user with id <num>
app.delete('/user/:userid', function (req, res) {
    var userid = parseInt(req.params.userid); // use same variable name. use parseInt
    if (isNaN(userid)) {
        res.status(404).json({ message: `Unacceptable record id` })
    } else {
        user.deleteUser(userid, function (err, result) {
            if (!err) {
                res.status(200).json(result);
            } else {
                res.status(500).json({ message: `Some error` });
            }
        });
    }
});

module.exports = app
