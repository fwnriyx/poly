// var jsObjectFormattedInJSON ={
//     "name":"John",
//     "age":"18",
//     "course":"DIT"
//  }

// console.log(jsObjectFormattedInJSON);

// var jsObjectFormattedInJSON ={
//     "name":"John",
//     "age":18, //JSON or JS the values can be a number
//     "course":"DAAA"
//  }

// console.log(jsObjectFormattedInJSON);

// var arrayOfJsonObjects = {"students": [
//         { "name": "John", "age": "18", "course": "DIT" },
//         { "name": "Mary", "age": "18", "course": "DISM" },
//         { "name": "Jack", "age": "28", "course": "NSFSW" }
//     ]}


// console.log(arrayOfJsonObjects);

// var student1={ //JSON object which is JS object
//     "name":"John",
//     "age": 18, // changed from "18" string to number
//     "course":"DIT"
//  };
 
//  console.log(student1.name);
//  console.log(student1.age);
//  console.log(student1.course);
 
// var jsObjectStudent ={ //JSON object which is JS object
//     name:"John",
//     age: 18, // changed from "18" string to number
//     course:"DAAA"
//  };
 
//  console.log(jsObjectStudent.name);
//  console.log(jsObjectStudent.age);
//  console.log(jsObjectStudent.course);
// console.log(jsObjectStudent);

// var jsonStringOfjsObjectStudent = JSON.stringify(jsObjectStudent)
// console.log(jsonStringOfjsObjectStudent);

// var jsObjectStudentConvertedFromJSON = JSON.parse(jsonStringOfjsObjectStudent);
// console.log(jsObjectStudentConvertedFromJSON);

// ff
var originalArray = [12, 34, 8712, 23, 1, 89];
var copyArray1 = originalArray;
var copyArray2 = [...originalArray]; //shallow copy of array
var copyArray3 = JSON.parse(JSON.stringify(originalArray)); //deep copy of array