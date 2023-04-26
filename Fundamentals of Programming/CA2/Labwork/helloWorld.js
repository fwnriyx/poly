/*
console.log("Hello World!");

console.log("She says, \'Hi!\' \nHe says, \"Bye\"\nMy dog\'s name is \"Clifford\"\nWhen do we use \\ backslash?\nA newline character is written like \"\\n\".");

console.log("She said. \"Let\'s try the rambutan bubble tea.\"");
// prints She said, "Let's try the rambutan bubble tea." 

console.log("1234\b");
console.log("1234\b5");
console.log("1234\b\b5");
console.log("\"The quick brown fox \n\tjumps over the \nlazy dog\"")  
console.log(" ____");
console.log("/.  .\\");
console.log("| \\/ |");
console.log("\\    /");
console.log(" ----");

console.log("I\'ve tried so hard \nand got so far and \nin the end it doesn't \neven matter.")



var area;
area = 6;
console.log(area);
*/

/*
var area = 6;
console.log("The area is " +area);

var fishName;
fishName = "Nemo"
console.log("My name is "+fishName);
fishLastName="Clown";
console.log("My name is ",fishName,fishLastName);

var fishAge;
fishAge = 6;
console.log("I am " +fishAge+ " years old");
fishAge = 6 + 1;
console.log("After one year, I will be " +fishAge+ " years old");

var x,y;
y=x
console.log(y)

console.log("Module Code\\Name: ST0502\\\”Fundamentals of Programming\”\n\t CA 1\t\t :40%\n\t CA 2\t\t :20%\n\t Exam\t\t :40%\n\t Total---------->:100%")


//Constants
const pi = 3.14159;
console.log(pi);

const secsInMin = 60
const minsInHours=60 

var walkMin;
var walkSec;

walkMin=5.5;

walkSec= walkMin * minsInHours;
console.log("I walked for " +walkSec+ " second(s)");


var totalStudents;
var num_not_in_group

totalStudents = 24;
num_not_in_group= total students % 2l
console.log("There is/are" +num_not_in_group+ "students who cannot form a group of 2." )
console.log("If there was zero students, that means the total numer of students is divisible by 2.")


var x = 20;
var y = 5;
z = x * y;
console.log("x  :" +x);
console.log("y  :" +y);
console.log("z  :" +z);

var input=require('readline-sync')

var userName = input.question('Enter your name:');
console.log( +userName+ "loves programming!");
var favColor= input.question('Enter your favorite color:');
console.log( +userName+ " loves Programming & " +favColor+ " color!")



var z = 10;
console.log("z is " + z +" before ");
console.log("z is " + --z);
console.log("z is " + z + "after");
*/
/*
//Question 9
var Celsius;
var Fahrenheit;  
var input = require('readline-sync');
var temperatureF = input.questionInt('Enter the temperature in Fahrenheit: ');
Celsius = 5/9 * ( temperatureF - 32); 

Celsius(.toFixed(0))

if ((Celsius >= 20) && (Celsius<=25)) {
console.log("The current room temperature is " +Celsius+ " degree Celsius");
}

//Next question(not labelled properly HAHA)
var input = require('readline-sync');
var intF = input.question('Enter first number: '); 
fNumber= parseFloat(intF)
var intS = input.question('Enter second number: ');
sNumber = parseFloat(intS)
var tNumber;
tNumber = fNumber + sNumber;

console.log("Here are the results...");

isDivisible = tNumber % + sNumber ==0
if(tNumber % +sNumber ==0) {
    console.log( tNumber + "divisible by " +sNumber+ "?" + isDivisible )
}



//Question 10

var input = require('readline-sync');

var year1= 1996
var year2= 1900
var isLeapYear1
var isLeapYear2
intYear1 = parseInt(year1);
intYear2 = parseInt(year2);
isLeapYear1 = ((intYear1 % 4 ==0) && (intYear1 % 100 !=0) || (intYear1 % 400 ==0));
isLeapYear2 = ((intYear2 % 4 ==0) && (intYear2 % 100 !=0) || (intYear2 % 400 ==0));
console.log(year1 + "is a leap year? " + isLeapYear1);
console.log(year2 + "is a leap year? " + isLeapYear2);


//Question 12

console.log("Welcome to this app for computing new salary");

var input = require('readline-sync');

var userName = input.question('Please enter your name: ');

console.log("\nHello " +userName + "! \n");

var salary = input.questionInt('Please enter your current salary: $');

var cSalary= parseInt(salary);

var nSalary;

if (cSalary < 1000) {
    nSalary = (120/100) * cSalary
}

if (cSalary < 2000 && (cSalary >= 1000)) {
    nSalary = (115/100) * cSalary
}

if (cSalary >= 2000) {
    nSalary = (110/100) * cSalary
}

var Increment= nSalary - cSalary;

intIncrement = parseInt(Increment);

intnSalary = parseInt(nSalary);

console.log("Heres the result: \n");

console.log("Current Salary \t\t  Increment \t\t New salary" );

console.log(+ cSalary + "\t\t\t  " + intIncrement+ "\t\t\t " +intnSalary);

//Optional Questions

//Q11)

var input = require('readline-sync');
var x1 = input.questionInt("Enter x1: ");
var x2 = input.questionInt("Enter x2: ");
var y1 = input.questionInt("Enter y1: ");
var y2 = input.questionInt("Enter y2: ");

var d= ((x2 - x1) **2 + (y2 - y1) **2) **0.5


console.log("The distance between (" +x1+ "," +y1+ ") and (" +x2+ "," +y2+ ") is " +d)


//Question 12

var input = require('readline-sync');

var fAngle = input.questionInt("First angle:");
var sAngle = input.questionInt("Second angle:");
var tAngle = 180 - fAngle - sAngle;
console.log("The third angle is " +tAngle+ " degrees");

//Question 13

var input= require('readline-sync');

var amount = input.questionInt("Enter amount ($) : ");


// Practical 3.

var input= require('readline-sync');

var fNumber= parseInt(input.question('Please enter 1st number: '));


var sNumber= parseInt(input.question('Please enter 2nd number: '));

if(isNaN(fNumber || sNumber)) {
    console.log("Sorry wrong input. Please try again. Good bye!")
}
 

if (fNumber > sNumber) {
    console.log("1st number is bigger")
}
 if (fNumber == sNumber) {
    console.log("Both numbers are equal")
}
 if (fNumber < sNumber) {
    console.log("2nd number is bigger.")
} 
else if(isNaN(fNumber, sNumber)) {
    console.log("Sorry wrong input. Please try again. Good bye!")
}


//Question 4
var input = require('readline-sync');

var score = parseInt(input.question("Please enter score: "))

if (score >= 80) {
    grade = 'A'
}
else if (score >= 70) {
    grade ='B'
}
else if (score >= 60) {
    grade = 'C'
}
else if (score >= 50) {
    grade = 'D'
}
else {
    grade= 'F'
}

console.log("Your grade is " + grade );



//Question 5

var input = require('readline-sync');

var nSalary;

var years = parseInt(input.question("Please enter your year(s) of service: "));

var salary = parseInt(input.question("Please enter your salary: $"));

if (years <10 && salary < 1000) {
    nSalary = salary + 100
}
else if (years <10 && salary < 2000) {
    nSalary = salary + 200
}
else if (years < 10 && salary >= 2000) {
    nSalary = salary + 300
}

if (years >= 10 && salary < 1000) {
    nSalary = salary + 200

}
else if(years >= 10 && salary < 2000) {
    nSalary = salary + 300
}
else if(years >= 10 && salary >=2000) {
    nSalary = salary + 400
}


var increment= nSalary - salary;

if (years <= 0 || salary <= 0) {
    console.log("Sorry invalid input(s). Please try again. Good bye!")
}
 else if(isNaN(years) || isNaN(salary)) {
    console.log("Sorry invalid input(s). Please try again. Good bye!")
 }
 else {
     console.log("Congratulations, your increment is: $" +increment );
 }
 


/*
//Question 6 income tax

var input = require('readline-sync');

var status = input.question("Please enter C for Citizen or F for foreigner: ")

var income = parseInt(input.question("Please enter your annual income: "));

if (status != 'C' && status != 'c' && status != 'F' && status != 'f')
 {
    console.log("Sorry wrong input. Please try again. Good bye!");
 }
else if (income < 0 || isNaN(income)) {
    console.log("Sorry wrong input. Please try again. Good bye!");
}
else {

    if (status == 'C', 'c' && income < 10000) {
        var tax = 100
    }
    else if (status == 'C', 'c' && income <= 25000) {
        tax = 105 / 100 * income - income
    }
    else if (status == 'C', 'c' && income > 25000) {
        tax = (115 / 100 * income) - income
    }

    if (status == 'F', 'f' && income < 8000) {
        var tax = 100
    }
    else if (status == 'F', 'f' && income <= 15000) {
        tax = 110 / 100 * income - income
    }
    else if (status == 'F', 'f' && income > 15000) {
        tax = 120 / 100 * income - income
    }

    console.log("Tax computed is " + tax);
}
*/
//Question 7; check number
/*
var input = require('readline-sync');
var int = parseInt(input.question('Enter an integer: '));
if (isNaN(int)) {
    console.log('Sorry wrong input. Please try again. Goodbye!');
}
else {
    if (int % 5 == 0 && int % 6 == 0) {
        console.log (int + ' is divisible by both 5 and 6.');
    }
    else if (int % 5 == 0 && int % 6 != 0) {
        console.log (int + ' is divisible by either 5 or 6, but not both.');
    }
    else if (int % 5 != 0 && int % 6 == 0) {
        console.log (int + ' is divisible by either 5 or 6, but not both.');
    }
    else if (int % 5 != 0 && int % 6 != 0) {
        console.log (int + ' is not divisible by either 5 or 6.');
    }
}

//Question 8
var input = require('readline-sync');

var rank = parseInt(input.question('Please enter your rank: '));

if (isNaN(rank) || rank <= 0) {
    console.log('Sorry wrong input. Please try again. Good bye!');
}
else{
    switch (rank) {
        case 1:
            console.log('Your prize money is $1000');
            break;
        case 2:
            console.log('Your prize money is $800');
            break;
        case 3:
            console.log('Your prize money is $700');
            break;
        case 4:
            console.log('Your prize money is $300');
            break;
        case 5:
            console.log('Your prize money is $300');
            break;
        default:
            console.log('Your prize money is $20');
    }
}

//Question 9(optional qn)

var input = require('readline-sync');
var bikeType = parseInt(input.question('Enter bicycle type: \n(1) Single seater (2) Double Seater\n >> '));


if(bikeType != 1 && bikeType != 2){
    console.log('Sorry wrong input. Please try again. Good bye!')
}
else {
    var duration = parseInt(input.question('Enter number of hours rented: '));

    if(duration <= 0 || isNaN(duration)) {
    console.log('Sorry wrong input. Please try again. Good bye!')
}
else {
    if(bikeType == 1) {
        var rentSPrice = 5.5 * duration;
    }
    else if(bikeType == 2) {
        var rentDPrice = 7.8 * duration;
    }
    if(bikeType == 1 && duration >= 3) {
        rentSPrice = 70/100 * rentSPrice;
        rentSPrice.toFixed(2); 
        console.log('Total rental fee: $' + rentSPrice);
    }
    if(bikeType == 2 && duration >= 3) {
        rentDPrice = 70/100 * rentDPrice;
        rentDPrice.toFixed(2);
        console.log('Total rental fee: $' + rentDPrice);
    }

}
}




var result = ' ';
for (var i = 3; i < 19; i+=3) {
    result = result + i + ' '
}
console.log(result)



var result = '-';
for(var i = 20; i > 0; i-=5){
    result = result + i + '-'
}
console.log('25' + result + '0');


var result = ' ';
for(var i = 1; i < 126; i**=3){
    result = result + i + ' '
}
console.log(result);


//Question 4a

for(var i = 1; i < 13; i++){
    var result = i * 5
    console.log(i + ' x 5 = ' + result);
}

//Question 5
var input = require('readline-sync');
var sum = 0
for(var i = 1; i < 6; i++) {
    var n = parseInt(input.questionInt("number "+ i + ": " )) 
    sum+=n        
}


console.log("Sum of numbers: " + sum)
*

var result = ' '
var input = require('readline-sync');
var fNumber = parseInt(input.question('Enter 1st number: '))
var sNumber = parseInt(input.question('Enter 2nd number: '))
var diff = fNumber - sNumber
if (diff < 0){
    for (var x =  fNumber + 1; x < sNumber;x++){
        if (x%2 == 1){
            result = result + x + ' '
            
        }
    }
} //negative number 
else {
    for (var x = sNumber + 1; x < fNumber; x++) {
        if(x%2 == 1){
            result = result + x + ' '
        }
    }
}
console.log(result);
*/
/*

//Q 2a
var s = ' '
var x = 1
while(x <=5) {
    var a = x * 6
    s = s + a + ' '
    x++;
}
console.log(s)

//Q 2b
var s = '-'
var x = 80
while (x >= 20) {
    var a = x / 2;
    x = x/2
    var s = s + a + '-'
}
console.log('80' + s + '5');

//Q 3a
/*
var s= ' '
var a = 1
do {
    x = 2**a; 
    s = s + x + ' ';
    a++;
}
while(a < 7);
console.log(s);


//Question 3c

var s= ''
var n = 91
int = parseInt(n)
do{
    int -=11
    if( int % 2 == 0) {
        var a = '+' + int 
    }
    else if(int % 2 != 0) {
       var b= '-' + int
    }
    s= b + a + ' ';
}
while( int > 46)
console.log (s);

/*
//Question 4
var input = require('readline-sync');
do{
    var children = parseInt(input.question("Please enter the number of children: "))
    if(isNaN(children) || children < 0 || children > 50) {
        console.log("Invalid number of children!\nPlease enter in the range of 0 to 50")
    }
    else {
        console.log("Input accepted! Program terminated...")
    }
}
while (children < 0);


//Question 5
var input = require('readline-sync');

do {
    var number = parseInt(input.question("Enter a number: "));
    if (isNaN(number) || number < 100 || number > 200) {
        console.log("Error! Please enter a number between 100 and 200");
    }
}
while (number > 200 || number < 100);
console.log("Input excepted. End of Program!");



//Question 6 
var input = require('readline-sync');



do {
    var number = parseInt(input.question("Enter any number or (0) to quit: "));
    var result = (number % 3 == 0 && number % 5 !=0 );
    if (isNaN(number)) {
        console.log("Invalid input. Please try again.")
    }
    else if (number % 3 == 0 && number % 5 != 0) {
        console.log(number + " is divisible by 3 but not 5?" + result);
    }
    else if (number % 3 != 0) {
        console.log(number + " is divisible by 3 but not 5?" + result);
    }
    else {
        console.log(number + " is divisible by 3 but not 5?" + result);
    }
} while (number != 0)
    console.log("Program terminated...")

//Question 7
var input = require('readline-sync');



do {
    var number = parseInt(input.question("Enter any number or (0) to quit: "));
    var result = (number % 3 == 0 && number % 5 !=0 );
    if (isNaN(number)) {
        console.log("Invalid input. Please try again.");
    }
    else if(number == 0) {
        console.log("Program terminated...");
    }
    else if(number < 50 || number >100) {
        console.log("Error: Out of range!");
    }
    else if (number % 3 == 0 && number % 5 != 0) {
        console.log(number + " is divisible by 3 but not 5? " + result);
    }
    else if (number % 3 != 0) {
        console.log(number + " is divisible by 3 but not 5? " + result);
    }
    else {
        console.log(number + " is divisible by 3 but not 5? " + result);
    }
} while (number != 0)


var arr1 = [-1, 0, 'one', '2', true, false, 5];
console.log(arr1[arr1.length + arr1[0]]);
console.log(arr1[arr1[1]]);
console.log(arr1.length);

//Class question
/*
var students = new Array("Greg", "Mary", "Devon", "James");

for (var i = 0; i <= 3; i++) {
    console.log(students[i]);
}
students.shift();
students.pop();
students.unshift("Matt");
students.push("your name");
console.log(students.slice(2 , 4));

var students = new Array("Greg", "Mary", "Devon", "James");
students.splice(2, 1, 'Elizabeth' , 'Artie');
console.log(students);



// Question 4
var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
var days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

for (var i = 0; i < months.length; i++) {
    console.log(months[i] + " has " + days[i] + " days.");
}

//Question 5
var input = require('readline-sync');

var students = new Array(6);
var sum = 0;

var a = 0;


for (var i = 0; i < students.length; i++) {
    var marks = parseInt(input.question("Enter marks for student #" + (i + 1) + ": "));
    
    if (marks >= 80) {
        a++
    }
    sum+=marks
}
if(isNaN(sum) || marks < 0 || marks >100) {
    console.log("Please input values again.")
}
else{
    var avg = sum / (students.length)
    console.log(a + " students scored A grade");
    console.log("The average mark is " + avg);
}

//Question 6
var list1 = new Array(12, 56, 76, 32, 12, 34);
var list2 = new Array(12, 56, 76, 32, 12, 34);

var sum;

if (list1.length != list2.length) {
    console.log("Two lists are not strictly identical");
}
else if (list1.length == list2.length) {
    for (var i = 0; i < list1; i++) {
        if (list1[i] == list2[i]) {
            sum++
        }
    }
}
if (sum == list1.length) {
    console.log("Two lists are strictly identical");
}

//Question 7
var intArray = new Array();

for (var i = 0; i <= 5; i++) {
    intArray.push(Math.floor(Math.random() * 11) + 1);
}

console.log("Elements of int array: " + intArray);

var max = intArray[0];


//Start of pract 6

for (var i = 1; i < intArray.length; i++) {
    if (intArray[i] > max)
    max = intArray[i];
    maxIndex =  i;
}
console.log("Highest value: " + max);

function evenNums()
{
    for(var i = 1; i < 21; i++){
        console.log(i);
    }
}
evenNums();



var input = require('readline-sync');

function isEvenNum(start, end) {

    console.log("Ensure that the first number is smaller than the second number.");
    var start = parseInt(input.question("Enter the first number: "));
    var end = parseInt(input.question("Enter the second number: "));

    if (isNaN(start)||isNaN(end)||start >= end) {
        console.log("Please enter the numbers again.");
    }
    else {
    for (var i = start; i <= end; i++) {
        if (i % 2 == 0) {
            console.log(i);
        }
    }
    }
}

isEvenNum(2,5);
 

var input = require ('readline-sync');

var s=' '

function allMultiple(num1, num2, x) {
     var num1 = parseInt(input.question("Enter the first number: "));
     var num2 = parseInt(input.question("Enter the second number: "));
     var x = parseInt(input.question("Enter the third number: "));
     for (var i = num1; i < num2; i++) {    
          if( i % x == 0) {
           s+=i + ' '
        }
    }
    console.log(s);
}

allMultiple();



//for random number, Math.floor(Math.random() * (big - small + 1)) + small

var i = (Math.floor(Math.random() * 69) + 0);
console.log(i);

var x = (Math.floor(Math.random() * 69) + 19);
console.log(x);

//Q6

function printTable() {
    for(i = 1; i <= 12; i++) {
        console.log(i + " x 5 = " + i*5);
    }
}

printTable();


//Q7
var input = require('readline-sync');

var rank;

function getInputs() {
    rank = parseInt(input.question('Please enter your rank: '));
    if (rank < 1 || isNaN(rank)) {
        console.log('Please input your rank again.');
    }
    else {
        return rank;
    }
        
}
function printPrize(rank) {
    switch (rank) {
        case 1:
            console.log('Your prize money is $1000');
            break;
        case 2:
            console.log('Your prize money is $800');
            break;
        case 3:
            console.log('Your prize money is $700');
            break;
        case 4:
            console.log('Your prize money is $300');
            break;
        case 5:
            console.log('Your prize money is $300');
            break;
        default:
            console.log('Your prize money is $20');
    }
}


getInputs();
printPrize(rank);




//Q8


//objects and classes
var circle1 = { radius: 10 };
var circle2 = { radius: 23 };
var circle3 = { radius: 125 };

console.log(circle1.radius + ',' + circle2.radius + ',' + circle3.radius);

circle2.radius = 25;
console.log(circle2.radius);

var area1 = (circle1.radius ** 2) * Math.PI;
var area2 = (circle2.radius ** 2) * Math.PI;
var area3 = (circle3.radius ** 2) * Math.PI;
var allArea = area1 + ' ' + area2 + ' ' + area3 + ' ';
console.log(allArea);


//Employee question

var employee1 = {
    name: "e1",
    age: 26,
    salary: 5000,
    sales: 50200
};
var employee2 = {
    name: "e2",
    age: 32,
    salary: 4600,
    sales: 55500
};

for (i = 0; i < 4 ; i++){

console.log(employee1[i] + employee2[i]);
}

employee1.name = "e3";
console.log(employee1.name);


//Question 7
class clubs {
    constructor(fees) {
        this.fees = fees;
    }
    getFees() {
        return 110/100 * this.fees;
    }
}
var sports = new clubs(50);
var commService = new clubs(0);
var foodies = new clubs(100);

console.log("Local fees to join the sports club is: " + sports.fees);
console.log("Local fees to join the Community service club is: " + commService.fees);
console.log("Local fees to join the foodies club is: " + foodies.fees);

console.log("Foreign Fees to join the sports club is: " + 110/100 * sports.fees);
console.log("Foreign Fees to join the community service club is : " + 110/100 * commService.fees);
console.log("Foreign fees to join the foodies club is: " + 110/100 * foodies.fees);

console.log("Foreign fees to join the sports club is: " + sports.getFees());
console.log("Foreign fees to join the community service club is: " + commService.getFees());
console.log("Foreign fees to join the foodies club is: " + foodies.getFees());


//Question 8

class rect {
    constructor(length, width) {
        this.length = length;
        this.width = width;
    }
    getArea() {
        return this.length * this.width;
    }
    getPerimeter() {
        return 2 * this.length + 2 * this.width;
    }
}

var r1 = new rect(10 , 5);

console.log("Area of rectangle r1 is " + r1.getArea());
console.log("Perimeter of rectangle r1 is " + r1.getPerimeter());

/
/
class Square{
    constructor(length){
         this.length = length;
    }
    calculateArea(){
         return this.length ** 2; 
    }
} 

var sqArray = [];

for (var i = 0; i < 11; i++) {
    var ran = Math.floor(Math.random() * 11) + 10;
    sqArray.push(ran);
    return sqArray
}

console.log(sqArray());

/*
function createSquareArray() {

    var len;
    var sqArray = [];

    for(var i = 0; i < 11; i++) {
        len = 10 + Math.floor(Math.random() * 11);
        sqArray.push(new sqArr1);
    }

    return sqArray;
} //createSquareArray

createSquareArray()
*/

//QUESTION 3

var input = require('readline-sync');
class Contact {
    constructor(name, mobileNumber) {
        this.name = name;
        this.mobileNumber = mobileNumber;
    }
    getContactDetails() {
        let cont = "Name = " + this.name + "\n" + "Mobile number: " + this.mobileNumber;
        return cont;
    }
}

class AddressBook {
    constructor() {
        this.mycontact = [];
        this.mycontact.push(new Contact("Homer", 98849959));
        this.mycontact.push(new Contact("Marge", 84774744));
        this.mycontact.push(new Contact("Lisa", 86994994));
        this.mycontact.push(new Contact("Maggie", 94775883));
        this.mycontact.push(new Contact("Bart", 88838848));
    }
    getNumberofContacts() {
        return this.mycontact.length;
    }
    getContactAt(index) {
        return this.myContact[index];
    }
    searchContact(searchName) {
        for (let i = 0; i < this.getNumberofContacts; i++) {
            if (searchName == this.getContactAt[i].name)
                return this.getContactAt[i].mobileNumber;
        }
    }
}
const myAddressBook = new AddressBook;
var input = require('readline-sync');
do {
    var choice = input.question("\nPersonal Addressbook\n" + "--------------\n" + "(1) Show all contacts\n" + "(2) Search Contact\n" + "(3) Exit\n" + ">>");

switch (choice) {
    case "1":
        showAllContact(myAddressBook);
        break;
    case "2":
        var searchName = input.question("Enter the name of the contact: ");
        console.log( searchName + "'s phone number is" + myAddressBook.searchContact.i);
        break;
    case "3":
        console.log("Goodbye!");
        break;
    default:
        console.log("********Invalid selection. Please try again.")
}
} while(choice != 3)
function showAllContact(myAddressBook) {
    i = 0;
    do {
        console.log("\n-------------------------------------");
        console.log("Contact" + (i + 1) + " of " + myAddressBook.getNumberofContacts());
        console.log("----------------------------------------");
        console.log(myAddressBook.getContactAt(i).getContactDetails());
        console.log("----------------------------------------");
    }
    while (scroll != "X" || scroll != "x")
}