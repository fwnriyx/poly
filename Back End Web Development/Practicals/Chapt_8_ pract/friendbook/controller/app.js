const express = require("express");
const app = express();

const user = require("../model/user");
const friendship = require("../model/friendship");
const post = require("../model/post");

const jwt = require("jsonwebtoken");
const JWT_SECRET = require("../config.js");
const isLoggedInMiddleware = require("../auth/isLoggedInMiddleware");

// Do in terminal "npm i cors"
// Check the dependancy in package.json
// Add-in the following 3 lines in app.js
// This 3 lines allows backend server to accept req from another domain
var cors = require('cors');
app.options('*',cors());
app.use(cors());

app.use(express.json());// parse application/json
app.use(express.urlencoded({ extended: false })); // parse application/x-www-form-urlencoded

// Endpoint for Login
app.post("/login/", (req, res) => {
    user.loginUser(
        req.body.username,
        req.body.password,
        (error, user) => {
            if (error) {
                res.status(500).send();
                return;
            } else if (user === null) {
                res.status(401).send();
                return;
            } else {
                const payload = { user_id: user.id };
                jwt.sign(payload, JWT_SECRET, { algorithm: "HS256" }, (error, token) => {
                    if (error) {
                        console.log(error);
                        res.status(401).send();
                        return;
                    } else {
                        res.status(200).send({
                            token: token,
                            user_id: user.id
                        });
                    }
                });
            }
        });
});

// Endpoint 03: GET /users/:userID/
app.get("/users/:userID/", isLoggedInMiddleware, (req, res, next) => {
    const userID = parseInt(req.params.userID);
    // if userID is not a number, send a 400.
    if (isNaN(userID)) {
        res.status(400).send();
        return;
    } else if (req.decodedToken.user_id == userID) {
        user.findByID(userID, (error, user) => {
            if (error) {
                res.sendStatus(500);
            } else if (user === null) {
                res.sendStatus(404);
            } else {
                res.status(200).json(user);
            }
        });
    } else {
        res.sendStatus(403);
    }
});

// Endpoint 01: GET /users/	
app.get("/users/", isLoggedInMiddleware, (req, res, next) => {
    user.findAll((error, users) => {
        // if (error) {
        //     console.log(error);
        //     res.status(500).send();
        // };
        // res.status(200).send(users);
        if (error) {
            res.sendStatus(500);
        } else if (users == null) {
            res.status(404).json({message: `No user found.`});
        } else {
            res.status(200).json(users);
        }
    });
});

// Endpoint 02: POST /users/
app.post('/users/',  function (req, res) {
    user.insert(req.body, function (err, result) {
        if (!err) {
            // console.log(result);
            res.status(201).json({message: `record <${result}> inserted!`})
        } else{
            res.sendStatus(500);
        }
    });
});

// Endpoint 04: PUT /users/:userID
app.put('/users/:userID', isLoggedInMiddleware, function (req, res) {
    var userID = parseInt(req.params.userID); // safer way to protect endpoint
    if (isNaN(userID)) { // this check is good for weeding out unacceptable inputs
        res.status(404).json({message: 'Unacceptable record requested'});
    } else if (req.decodedToken.user_id == userID) {
        user.edit(userID, req.body, function (err, result) {
            if (!err) {
                res.sendStatus(204);
            }else{
                res.sendStatus(500);
            }
        });
    } else {
        res.sendStatus(403);
    }
});

// Endpoint 00: DELETE /users/:userID
app.delete('/users/:userID', isLoggedInMiddleware, function (req, res) {
    var userID = parseInt(req.params.userID); // safer way to protect endpoint
    if (isNaN(userID)) { // this check is good for weeding out unacceptable inputs
        res.status(404).json({message: 'Unacceptable record requested'});
    } else if (req.decodedToken.user_id == userID) {
        user.delete(userID, function (err, result) {
            if (!err) {
                res.status(200).json({message: `${result} record deleted`});
            }else{
                res.status(500).json({message: 'Some error'});
            }
        });
    } else {
        res.sendStatus(403);
    }
});

// Endpoint 05: GET /users/:userID/friends
app.get('/users/:userID/friends', isLoggedInMiddleware, (req, res, next) => {
    const userID = parseInt(req.params.userID);
    if (isNaN(userID)) {
        res.sendStatus(400);
    } else if (req.decodedToken.user_id == userID ) {
        friendship.showFriends(userID, (error, results) => {
            if (error) {
                res.sendStatus(500);
            } else if (user === null) {
                res.sendStatus(404);
            } else {
                res.status(200).json(results);
            }
        });
    } else {
        res.sendStatus(403);
    }
});

// Endpoint 06: POST /users/:userID/friends/:friendID
app.post('/users/:userID/friends/:friendID', isLoggedInMiddleware, function (req, res) {
    const userID = parseInt(req.params.userID); // safer way to protect endpoint
    const friendID = parseInt(req.params.friendID); 
    if (isNaN(userID) || isNaN(friendID)) { // this check is good for weeding out unacceptable inputs
        res.status(404).json({message: 'Unacceptable record requested'});
    } else if (req.decodedToken.user_id == userID) {
        friendship.addFriend(userID, friendID, function (err, result) {
            if (!err) {
                res.status(201).json({message: `${result} record(s) inserted!`})
            } else{
                res.sendStatus(500);
            }
        });
    } else {
        res.sendStatus(403);
    }
});

// Endpoint 07: DELETE /users/:userID/friends/:friendID

// Endpoint 09: POST /posts
app.post('/posts', isLoggedInMiddleware, (req, res, next) => {
    post.insertUserPost(req.decodedToken.user_id, req.body.text_body, (error, results) => {
        if (error) {
            res.sendStatus(500);
        } else if (results === null) {// send a 404 if affectedRows is zero.
            res.sendStatus(404);
        } else {
            res.status(201).json({postID: results.insertId});
        }
    });
});

// Endpoint 10: GET /posts/:postID
app.get('/posts/:postID', (req, res, next) => {
    const postID = parseInt(req.params.postID);
    if (isNaN(postID)) {
        res.sendStatus(400);
    } else {
        post.getPostByID(postID, (error, posts) => {
            if (error) {
                res.sendStatus(500);
            } else if (posts === null) {// send a 404 if friend is not found.
                res.sendStatus(404);
            } else {
                res.status(200).json(posts[0]);
            }
        });
    }
});

// Endpoint 15: GET /users/:userID/posts
app.get('/users/:userID/posts', isLoggedInMiddleware, (req, res, next) => {
    const userID = parseInt(req.params.userID);
    if (isNaN(userID)) {
        res.sendStatus(400);
    } else if (req.decodedToken.user_id == userID) {
        post.getUserPosts(userID, (error, posts) => {
            if (error) {
                res.sendStatus(500);
            } else if (posts === null) {// send a 404 if friend is not found.
                res.sendStatus(404);
            } else {
                res.status(200).json(posts);
            }
        });
    } else {
        res.sendStatus(403);
    }
});



module.exports = app;
