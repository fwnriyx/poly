const isSorted = require('is-sorted');
console.log(isSorted([1, 2, 3, 4, 5]));
console.log(isSorted([1, 5, 2, 4]));
console.log(isSorted([1, 3, 10, 50]));

const john = require('./file');

console.log(john); //John is a JS object
console.log(JSON.stringify(john)); // this is now a JSON formatted string


// var newCopyofArray = JSON.parse(JSON.stringify(array)) deep copy of array

