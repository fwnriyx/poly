var user = require('../model/user');
var express = require('express');
var app = express();

app.use(express.urlencoded({ extended: false }));//attach body-parser middleware
app.use(express.json());//parse json data

// Version B
app.use(function (req, res, next) {//create our custom middleware
    const { method, url, path, query } = req;
    console.log(`Method: ${method} URL: ${url}`);
    next();
}); // a good idea as a debugging tool

//VERB+URL defines the endpoint
//longer url goes first
// Endpoint 0
app.get('/api/user/:id', function (req, res) {
    const id = parseInt(req.params.id); // data validation is usually expected
    if (isNaN(id)) {
        res.status(400).type("json").end(
            JSON.stringify({message: `Bad Request`})
        );
    } else {
        user.retrieveUser(id, (error, result) => {
            if (error) {
                res.status(404).type("json").end(
                    JSON.stringify({message: `User not found!`})
                );
            } else {
                res.status(200).type("json").end(
                    JSON.stringify(result)
                );
            }
        });
    }
});

// Endpoint 1
app.get('/api/user', function (req, res) {
    user.retrieveAllUser((error, result) => {
        if (error) {
            res.status(404).type(".json").end(
                JSON.stringify({ message: `User not found!` })
            );
        } else {
            res.status(200).type(".json").end(
                JSON.stringify(result)
            );
        }
    })
});

// Endpoint 02
//assume user has a username, email, role(admin/user) and password
app.post('/api/user', function (req, res) {
    const { password, username, role, email } = req.body;
    // res.status(200).type(".html").end(`
    //     <h1>
    //         Received new user data:
    //         </br>UserName${username}
    //         </br>Email${email}
    //         </br>Role${role}
    //         </br>Password${password}
    //     </h1>
    // `);
    res.status(200).type(".html").end(`
        <h1>
            Received new user data:
            </br>UserName: ${username}
            </br>Email: ${email}
            </br>Role: ${role}
            </br>Password: ${password}
        </h1>
    `);
});

// Endpoint 3
// Delete - Delete a resource
// METHOD Delete => http://localhost:8081/user/:id
app.delete('/user/:id', function (req, res) {
    const id = parseInt(req.params.id);
    if (isNaN(id)) {
        res.status(400).type(".json").end(
            JSON.stringify({ message: `Bad Request` })
        );
    } else {
        // http status code 200
        // {“message”: “User with <id> has been successfully deleted!”}
        res.status(200).type(".json").end(
            JSON.stringify({ message: `User with <${id}> has been successfully deleted!` })
        )
    }
});

// Endpoint 4
// PUT – update a resource 
// METHOD PUT => http://localhost:8081/user/:id
app.put('/user/:id', function (req, res) {
    const id = parseInt(req.params.id); // data validatin is usually expected
    if (isNaN(id)) {
        res.status(400).type(".json").end(
            JSON.stringify({ message: `Bad Request` })
        );
    } else {
        const {email, password} = req.body;
        res.status(200).type(".json").end(
            JSON.stringify({ message: `User with <${id}> has been successfully updated with new email <${email}>!` })
        );
    }
});

app.all('*',(req, res) => { // catch all to reply back to user as a response object
    const {method, url} = req; // works to help you get the right info for debugging
    res.status(400).type(".json").end(
        JSON.stringify({ message: `Bad Request: Method =${method} and URL = ${url}!` })
    );
})

module.exports = app;