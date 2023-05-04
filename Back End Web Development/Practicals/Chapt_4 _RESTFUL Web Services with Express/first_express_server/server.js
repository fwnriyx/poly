// Version 1
// var express = require('express');
// var serveStatic = require('serve-static');
// var app = express();
// var port=3000;
// var hostname="localhost";

// app.use(serveStatic(__dirname + '/public')); //apply middleware with app.use
// app.listen(port, hostname, () => {
//     console.log(`Server started and accessible via http://${hostname}:${port}/`);
//   });

//Version 2
// var express = require('express');
// var app = express();
// var port = 3000;

// //Version A (similar to Version 1)
// app.use(function(req, res, next) {//create our custom middleware
//     console.log(req.url);
//     console.log(req.method)
//     console.log(req.path);    
//     console.log(req.query.id);
//     next();
//   }); // a good idea as a debugging tool

//Version B
// app.use(function(req, res, next) {//create our custom middleware
//     const {method, url, path, query} = req;
//     console.log(`Method: ${method} URL: ${url} Path: ${path} Query: ${query.id}`);
//     next();
//   }); // a good idea as a debugging tool

//Version C
var express = require('express');
var app = express();
var port = 3000;
app.use(function (req, res, next) {
    const { method, url, path, query } = req;
    console.log(`Method: ${method} URL: ${url} Path: ${path} Query: ${query}`);
    // res.status(200);
    // res.type(".html");
    // res.end("<html><body><h1>Using response object!!</h1></body></html>");

    res.status(200).type(".html").end(`
    <html>
        <body>
            <h1>Using response object!!</h1>
        </body>
    </html>
    `);
    //res.redirect("https://www.sp.edu.sg");//comment out if we just want to redirect

    //next();//since we are setting the whole response data, do not pass to the next middleware
});



app.use(express.static('public')); //apply middleware with app.use

app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});