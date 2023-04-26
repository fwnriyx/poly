//P2222811 Muhammad Fitri Amir bin Abdullah DAAA/FT/1B/06

var app = require('./controller/app.js');
var express = require('express')

var port = 3000;

app.use(express.static('images/product'));


app.listen(port, function() {
    console.log(`SP DVD Server started on http://localhost:${port}/`);
})