//LETS FUCKING GOOOOOOOOOOOOO
var input = require('readline-sync');
/*
//Question 1(big bus)

var max;
var n = parseInt(input.question("Enter a positive number: "));

function bigBus(n){
    var busArray = [];

    for(i = 1; i <= n; i++) {
        if (i % 15 == 0){
            busArray.push("Big bus");
        }
        else if (i % 5 == 0){
            busArray.push("Bus");
        }
        else if (i % 3 == 0) {
            busArray.push("Big");
        }
        else {
            busArray.push(i);
        }
    }
    return busArray;
}



console.log(bigBus(n));
*/


//Question 2(max number)
//Qn 2

const numbers = [5,1,3,5,10,2,41,4];
 
function maxNumber(x) {
    let y = x[0];
    for (i = 0; i < x.length; i++) {
        if (x[i] > y) {
            y = x[i];
        }
    }
    return y;
}

console.log(maxNumber(numbers)); //41


/*
//Question 3(Multiplication table)

var n = parseInt(input.question("Enter a number: "));

function multiplicationTable(n) {
    var mainArray = [];
    for (i = 1; i <= n; i++) {
        var timesArray = [];
        for (m = 1; m <= n; m++) {
            var result = i * m;
            timesArray.push(result);
        }
        mainArray.push(timesArray);
    }
    return mainArray;
}

console.log(multiplicationTable(n));
*/

//Question 4(mean)

// function calculateMean(numbers){
//     var total = 0;
//     for(i = 0; i < numbers.length; i++){
//         total += numbers[i]; 
//     }
//     var mean = total/(numbers.length);
//     return mean
// }

// const numbers = [1, 2, 3, 4, 5];

// console.log(calculateMean(numbers));

// //Question 5 (fib numbers)

// function fib(num) {
//     var fArray = [0, 1]

//     if (num < 2) {
//         return fArray[num];
//     }

//     else {
//         for (n=1; n<num; n++) {
//             var fNumber = fArray[n] + fArray[n-1];
//             fArray.push(fNumber);
//         }

//         return fNumber;
//     }
// }
// const fib = (num) => {
//     if (num < 2) return num;
//     return fib(num - 1) + fib(num - 2);
// }

// console.log(fib(0));
// console.log(fib(1));
// console.log(fib(2));
// console.log(fib(3));
// console.log(fib(4));

// const fib = (num) => {
//     var [a, b] = [0, 1];
//     while(num--) {
//         [a, b] = [b, a + b]
//     }
//     return a 
// }

// console.log(fib(50));
// main program
// console.log(fib(8))

// Question 6(two sum)

//  twosum = function (numbers, sum) {
//     for(i = 0; i < numbers.length; i++){
//         for(i1 = 1; i1 < numbers.length; i++){
//             if(numbers[i1]+numbers[i] == sum){
//                 return [i, i1];
//             }
//         }
//     }
//     return -1
// }

// var numArray = [2, 8, 11, 13];
// console.log(twosum(numArray, 19))

//Question 7(same characters)


// function commonCharacters(word1, word2){
//     var word1Array = word1.split("");
//     var word2Array = word2.split("");
//     var letters = [];
//     for (i = 0; i < word1Array.length; i++) {
//         for (i1 = 0; i1 < word2Array.length; i1++){
//             if (word1Array[i] == word2Array[i1]){
//                 letters.push(word1Array[i]);
//             }
//         }
//     }
//     return letters
// }

// console.log(commonCharacters("jjoohn", "ron"))

