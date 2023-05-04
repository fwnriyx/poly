var app = require('./controller/app.js');

var port = 8081;//use another port 8081 for this exercise
var hostname = "localhost";

app.listen(port, hostname, () => {
    console.log(`Server started and accessible via http://${hostname}:${port}/`);
  });