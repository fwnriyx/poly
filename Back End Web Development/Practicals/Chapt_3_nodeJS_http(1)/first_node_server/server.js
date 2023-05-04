const http = require('http');
const fs = require('fs');
const path = require('path');

const hostname = 'localhost'; // IP address
const port = 3000; //TCP port number

//request and response parameter
// const server = http.createServer((req, res) => {
//     res.statusCode = 200;
//     res.setHeader('Content-Type', 'text/html');// html encoded response
//     res.end(`
//         <html>
//             <body>
//                 <h1>Welcome to my first Node JS server!</h1>
//             </body>
//         </html>
//     `);
// });


//Version 2
// const server = http.createServer((req, res) => {
//     console.log('Request for page ' + req.url + ' using ' + req.method + 'method');
//     if (req.method == 'GET') {
//       var fileUrl = req.url;

//       if (req.url == '/') //default file is index.html
//         fileUrl = '/index.html';

//       var filePath = path.resolve('./public'+fileUrl);

//         fs.exists(filePath, (exists) => {
//             if (!exists) {
//                 fileUrl='/error.html';
//                 filePath = path.resolve('./public'+fileUrl);
//                 res.statusCode = 404; //404 error not found
//                 res.setHeader('Content-Type', 'text/html');
//             }else{
//                 res.statusCode = 200; //200 = created
//                 res.setHeader('Content-Type', 'text/html');
//             }
//             fs.createReadStream(filePath).pipe(res);
//         });
//     }
//     else {
//         fileUrl='/error.html';
//         filePath = path.resolve('./public'+fileUrl);
//         res.statusCode = 500;//Internal Server Error
//         res.setHeader('Content-Type', 'text/html');
//         fs.createReadStream(filePath).pipe(res);

//     }
// });

//Version 3
const server = http.createServer((req, res) => {
    const { headers, method, url } = req; //use this style of extracting the needed attributes
    let body = [];

    req.on('error', (err) => {
        console.error(err);
    }).on('data', (chunk) => {
        body.push(chunk);
    }).on('end', () => {
        body = Buffer.concat(body).toString(); //assume tht the file is too big

        console.log(`Method: ${method} URL: ${url} Body: ${body}`); //use console.log as a "system log" for example Get abc.com
        // console.log(body.length);
        // At this point, we have the headers, method, url and body, and can now
        // do whatever we need to in order to respond to this request.
        if (req.method == 'GET') {
            var fileUrl = req.url;

            if (req.url == '/') //default file is index.html
                fileUrl = '/index.html';

            var filePath = path.resolve('./public' + fileUrl);

            fs.exists(filePath, (exists) => {
                if (!exists) {
                    fileUrl = '/error.html';
                    filePath = path.resolve('./public' + fileUrl);
                    res.statusCode = 404; //404 error not found
                    res.setHeader('Content-Type', 'text/html');
                } else {
                    res.statusCode = 200; //200 = created
                    res.setHeader('Content-Type', 'text/html');
                }
                fs.createReadStream(filePath).pipe(res);
            });


        } else if (req.method == 'POST') {
            //LOGIN - create a resource
            // METHOD POST => http://localhost:3000/login
            if (url == '/login') {
                // BODY => {“user”: “admin@abc.com”, “password”: “1234567”}
                const { user, password } = JSON.parse(body); // change back to JSON object
                if ((user == 'admin@abc.com') && (password == '1234567')) {
                    //http status code 200
                    // {'message': 'Welcome admin!'}
                    res.statusCode = 200;//Unprocessable Entity
                    res.setHeader('Content-Type', 'text/json');
                    res.end(JSON.stringify({ message: 'Welcome admin!' }));
                }
                } else {
                    fileUrl = '/index.html';
                    var filePath = path.resolve('./public' + fileUrl);
                    res.statusCode = 200; //200 = created
                    res.setHeader('Content-Type', 'text/html');
                    fs.createReadStream(filePath).pipe(res);
                }      
        } else if (req.method == 'PUT') {
            res.statusCode = 422;//Unprocessable Entity
            res.setHeader('Content-Type', 'text/json');
            res.end(JSON.stringify({ message: 'Not Implemented Yet' }));
        } else if (req.method == 'DELETE') {
            res.statusCode = 422;//Unprocessable Entity
            res.setHeader('Content-Type', 'text/json');
            res.end(JSON.stringify({ message: 'Not Implemented Yet' }));
        } else { // catch all for commands/verbs/methods that are not GET, POST, PUT, DELETE
            fileUrl = '/error.html';
            filePath = path.resolve('./public' + fileUrl);
            res.statusCode = 500;//Internal Server Error
            res.setHeader('Content-Type', 'text/html');
            fs.createReadStream(filePath).pipe(res);
        };
    });
});
server.listen(port, hostname, () => {
    console.log(`Server started and accessible via http://${hostname}:${port}/`);
});  
