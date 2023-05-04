var express = require('express');
var app = express();
var user = require('../model/user.js');
var verifyToken = require('../auth/verifyToken.js')

// var bodyParser = require('body-parser');
// var urlencodedParser = bodyParser.urlencoded({ extended: false });
// app.use(bodyParser.json());// parse application/json
// app.use(urlencodedParser); // parse application/x-www-form-urlencoded

app.use(express.json());// parse application/json
app.use(express.urlencoded({ extended: false })); // parse application/x-www-form-urlencoded

// Endpoint 0 POST /login
app.post('/login', function (req, res) {
    var email = req.body.email;
    var password = req.body.password;
    user.loginUser(email, password, function (err, result) {
        if (!err) {
            // res.send("{\"result\":\"" + result + "\"}");
            res.status(200).json({ token: result })
        } else {
            res.status(500);
            res.send(err.statusCode);
        }
    });
});

// Endpoint 1	GET /user/:userid	    empty	Retrieve data of user with id <num>
app.get('/user/:userid', verifyToken, function (req, res) { // url MUST follow specified requirements
    // var id = req.params.userid; // it is better to use the same variable for ease of debugging
    // var userid = req.params.userid; // better but can be improved
    var userid = parseInt(req.params.userid);

    if (isNaN(userid)) {
        res.status(404).json({ message: `Unacceptable record ID` });
    } else if ((req.userid == userid) || (req.role == 'admin')) {
        user.getUser(userid, function (err, result) {
            if (!err) {
                if (result.length == 0) {
                    res.status(200).json({ message: `Record not found` });
                } else {
                    // res.send(result); // BED usually use JSON
                    res.status(200).json(result);
                }
            } else {
                res.status(500).json({ message: `Some error` });
            }
        });
    } else {
        res.status(403).json({ message: 'not authorised' });
    }
});

// Endpoint 2	GET /user			    empty	Retrieve data of all users
app.get('/user', verifyToken, function (req, res) { // url MUST follow specified requirements
    if (req.role == 'admin') {
        user.getUsers(function (err, result) {
            if (!err) {
                if (result.length == 0) {
                    res.status(200).json({ message: `Record not found` });
                } else {
                    // res.send(result); // BED usually use JSON
                    res.status(200).json(result);
                }
            } else {
                res.status(500).json({ message: `Some error` });
            }
        })
    } else {
        res.status(403).json({ message: 'not authorised' });
    }
});

// Endpoint 3	POST /user		        JSON    String of user details	Insert new user record
app.post('/user', function (req, res) { // url MUST follow specified requirements
    // var username = req.body.username;
    // var email = req.body.email; 
    // var role = req.body.role;
    // var password = req.body.password;

    // Version 1
    var { username, email, role, password, profile_pic_url } = req.body;
    user.addUser(username, email, role, password, profile_pic_url, function (err, result) {
        if (!err) {
            // console.log(result);
            // res.status(200).json({message: `${result} record inserted`}); // less common
            res.status(200).json({ message: `New record with ID <${result}> inserted` }); // more common
        } else {
            res.status(500).json({ message: `Some Error` });
        }
    });

    // Version 2
    // user.addUser(req.body, function (err, result) {
    //     if (!err) {
    //         console.log(result);
    //         res.status(200).json({message: `${result} record inserted`});
    //     } else{
    //         res.status(500).json({message: `Some Error`});
    //     }
    // });

});

// Endpoint 4	PUT /user/:userid	    JSON    String of updated user details	Update user with id <num>
app.put('/user/:userid', verifyToken, function (req, res) { // url MUST follow specified requirements
    var userid = parseInt(req.params.userid);
    var { email, password } = req.body;
    if (isNaN(userid)) {
        res.status(404).json({ message: `Unacceptable record ID` });
    } else if ((req.usereid == userid) || (req.role == 'admin')){
        user.updateUser(email, password, userid, function (err, result) {
            if (!err) {
                res.status(200).json({ message: `${result} record updated` });
            } else {
                res.status(500).json({ message: `Some error` });
            }
        });
    } else {
        res.status(403).json({ message: 'not authorised' });
    }
});

// Endpoint 5	DELETE /user/:userid	empty	Delete user with id <num>
app.delete('/user/:userid', verifyToken, function (req, res) { // url MUST follow specified requirements
    var userid = parseInt(req.params.userid);
    if (isNaN(userid)) {
        res.status(404).json({ message: `Unacceptable record ID` });
    } else if (req.role == 'admin'){
        user.deleteUser(userid, function (err, result) {
            if (!err) {
                res.status(200).json({ message: `${result} record deleted` });
            } else {
                res.status(500).json({ message: `Some error` });
            }
        });
    } else {
        res.status(403).json({ message: 'not authorised' });
    }
});


module.exports = app
