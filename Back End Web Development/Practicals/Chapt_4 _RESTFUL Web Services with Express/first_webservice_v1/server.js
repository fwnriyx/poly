// //Version 1
// var express = require('express');
// var bodyParser = require('body-parser');
// var port = 8081;//use another port 8081 for this exercise
// var hostname="localhost";

// var app = express();

// var urlencodedParser = bodyParser.urlencoded({ extended: false });
// app.use(urlencodedParser);//attach body-parser middleware
// app.use(bodyParser.json());//parse json data

// //Version B
// app.use(function(req, res, next) {//create our custom middleware
//     const {method, url, path, query} = req;
//     console.log(`Method: ${method} URL: ${url}`);
//     next();
//   }); // a good idea as a debugging tool

// //VERB+URL 
// app.get('/api/user', function (req, res) {

//    res.status(200);
//    res.type(".html");
//    res.end("Data of all users sent!");
// });

// app.listen(port, hostname, () => {
//     console.log(`Server started and accessible via http://${hostname}:${port}/`);
//   });

//Version 2
var express = require('express');

var bodyParser = require('body-parser');
var port = 8081;//use another port 8081 for this exercise
var hostname = "localhost";

var app = express();
app.use(express.urlencoded({ extended: false }));//attach body-parser middleware
app.use(express.json());//parse json data

//Version B
app.use(function (req, res, next) {//create our custom middleware
    const { method, url, path, query } = req;
    console.log(`Method: ${method} URL: ${url}`);
    next();
}); // a good idea as a debugging tool

//VERB+URL defines the endpoint

//Endpoint 1
app.get('/api/user', function (req, res) {
    res.status(200).type(".html").end(`
        <h1>
            Data of all users sent!
        </h1>
    `);
});

//Endpoint 2
//assume user has a username, email, role(admin/user) and password
app.post('/api/user', function (req, res) {
    const{password, username, role, email} = req.body;
    res.status(200).type(".html").end(`
        <h1>
            Received new user data:
            </br>UserName${username}
            </br>Email: ${email}
            </br>Role: ${role}
            </br>Password: ${password}
        </h1>
    `);
});

app.listen(port, hostname, () => {
    console.log(`Server started and accessible via http://${hostname}:${port}/`);
});