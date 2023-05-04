
// function funct1() {
//     console.log("Printing!!");
// }
// console.log("Running function funct1")
// funct1();

// const funct1 = () => {
//     console.log("Printing!!");
// }
// console.log("Running function funct1")
// funct1();

// Illustrate higher order function, cn pass funct as argument to another funct
// setInterval(function(){
//     console.log('Running...');
// }, 1000);

// var walk = function() {
//     console.log('Walking...');
// }
// setInterval(walk, 1000)

// var jog = () => {
//     console.log("Jogging...");
// }
// setInterval(jog, 1000); 

// function firstFn() {
//     console.log(1)
// }
// function secondFn(){
//     console.log(2)
// }

// firstFn();
// secondFn();

// function firstFn(){
//     // Simulate a code delay
//     setTimeout( function(){
//     console.log(1);
//     }, 2000 );
// }

// function secondFn(){
//     console.log(2);
//     }


// firstFn();
// secondFn();

// const fs = require('fs');
// fs.readFile('./file.txt','utf-8', function(err, data){
//     if (err !== null) {
//         //handle error
//         console.log(err)
//     }else
//     console.log(data);
// })

// const fs = require('fs');
// fs.readFile('/file.txt', 'utf-8',(err, data)=>
//     {
//         if (err !== null){
//             //handle error
//             console.log(err)
//         }else {
//             //no errors, process data
//             console.log(data)
//         }
//     })