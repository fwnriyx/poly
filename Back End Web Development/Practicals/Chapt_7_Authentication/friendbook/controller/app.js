const express = require("express");
const app = express();

// import the model files
const user = require("../model/user");
const friendship = require("../model/friendship");

const jwt = require('jsonwebtoken')
const JWT_SECRET = require('../config.js')
const isLoggedInMiddleware = require('../auth/isLoggedInMiddleware.js')

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

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
                })
            }
        });
});



// Endpoint 05: GET /users/:userID/friends Join-table
app.get("/users/:userID/friends", isLoggedInMiddleware, (req, res) => {
    const userID = parseInt(req.params.userID);
    // if userID is not a number, send a 400.
    if (isNaN(userID)) {
        res.sendStatus(400);
    } else if (req.decodedToken.user_id == userID){
        friendship.showFriends(userID, (error, user) => {
            if (error) {
                res.sendStatus(500);
            } else if (user === null) {
                res.status(404).json({ message: `Record not found` });
            } else {
                res.status(200).json(user[0]);
            }
        });
    } else {
        res.sendStatus(403);
    }
});

// Endpoint 03: GET /users/:userID/
app.get("/users/:userID/", isLoggedInMiddleware, (req, res, next) => {
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
    } else {
        res.sendStatus(403);
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
app.delete('/user/:userid', isLoggedInMiddleware, function (req, res) {
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
    } else {
        res.sendStatus(403);
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
            res.status(201).json({
                message:
                    `New user id <${results.newRecordId}> was created on ${results.created_at}`
            });
        }
    });
});

// Endpoint 04: PUT /users/:userID/
app.put("/users/:userID/", isLoggedInMiddleware, (req, res, next) => {
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
    } else {
        res.sendStatus(403);
    }
});

module.exports = app;







