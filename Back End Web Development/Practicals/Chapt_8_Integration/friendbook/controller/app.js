const express = require("express");
const app = express();

// import the model files
const user = require("../model/user.js");
const friendship = require("../model/friendship.js");
const posts = require("../model/post.js")

const jwt = require('jsonwebtoken');


var cors = require('cors');
app.options('*',cors());
app.use(cors());

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Endpoint 05: GET /users/:userID/friends Join-table
app.get("/users/:userID/friends", (req, res) => {
    const userID = parseInt(req.params.userID);
    // if userID is not a number, send a 400.
    if (isNaN(userID)) {
        res.sendStatus(400);
    } else {
        friendship.showFriends(userID, (error, friends) => {
            if (error) {
                res.sendStatus(500);
            } else if (user === null) {
                res.status(404).json({ message: `Record not found` });
            } else {
                res.status(200).json(friends);
            }
        });
    }
});

// Endpoint 03: GET /users/:userID/
app.get("/users/:userID/", (req, res, next) => {
    const userID = parseInt(req.params.userID);
    // if userID is not a number, send a 400.
    if (isNaN(userID)) {
        res.sendStatus(400);
    } else if (req.decodedToken.user_id == userID) {
        user.findByID(userID, (error, user) => {
            if (error) {
                res.sendStatus(500);
            } else if (user === null) {
                res.status(404).json({ message: `Record not found` });
            } else {
                res.status(200).json(user);
            }
        });
    }
});

// Endpoint 01: GET /users/
app.get("/users/", (req, res, next) => {
    user.findAll((error, users) => {
        if (error) {
            console.log(error);
            res.sendStatus(500);
        } else if (users == null) {
            res.sendStatus(204);
        } else {
            res.status(200).json(users);
        }
    });
});

// Endpoint 07: DELETE /users/:userID/friends/:friendID
// Endpoint 00: DELETE /users/:userID/
app.delete('/user/:userid', function (req, res) {
    var userid = parseInt(req.params.userid); // use same variable name. use parseInt
    if (isNaN(userid)) {
        res.status(404).json({ message: `Unacceptable record id` })
    } else if (req.decodedToken.user_id = userID){
        user.delete(userid, function (err, result) {
            if (!err) {
                res.sendStatus(204);
            } else {
                res.sendStatus(500);
            }
        });
    } 
});

// Endpoint 06: POST /users/:userID/friends/:friendID
// Endpoint 02: POST /users/
app.post("/users/", (req, res, next) => {
    user.insert(req.body, (error, results) => {
        if (error) {
            //console.log(error);
            res.sendStatus(500);
        } else {
            res.status(201).json({message:
                    `New user id <${results.newRecordId}> was created on ${results.created_at}`});
        }
    });
});

// Endpoint 04: PUT /users/:userID/
app.put("/users/:userID/", (req, res, next) => {
    const userID = parseInt(req.params.userID);
    if (isNaN(userID)) {
        res.sendStatus(400);
    } else if (req.decodedToken.user_id == userID){
        user.edit(userID, req.body, (error) => {
            if (error) {
                // console.log(error);
                res.sendStatus(500);
            } else {
                res.sendStatus(204);
            }
        });
    }
});


//Endpoint 15: GET/users/:userID/posts
app.get("/users/:userID/posts", (req, res, next) => {
    const userID = parseInt(req.params.userID);
    // if userID is not a number, send a 400.
    if (isNaN(userID)) {
        res.sendStatus(400);
    } else {
        posts.getUserPosts(userID, (error, posts) => {
            if (error) {
                res.sendStatus(500);
            } else if (user === null) {
                res.status(404).json({ message: `Record not found` });
            } else {
                res.status(200).json(posts);
            }
        });
    }
});

module.exports = app;







