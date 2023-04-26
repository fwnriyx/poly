var Daytoday = new Date(); //date that is displayed on the calendar(for me its 7 august)
//to display daily events
var dailyevents = new Array()
dailyevents[1] = "<br />FOP CA2 + Quiz Submission ";
dailyevents[2] = "<br />CAT presentation";
dailyevents[3] = "<br /> Water training @ Reservoir";
dailyevents[4] = "<br />Personal gym training";
dailyevents[5] = "";
dailyevents[6] = "<br /> Water and endurance training";
dailyevents[7] = "";
dailyevents[8] = "<br />FED CA2 Submission ";
dailyevents[9] = "<br />National Day Holiday";
dailyevents[10] = "";
dailyevents[11] = "<br />CPR presentation";
dailyevents[12] = "<br />FOC CA2 Submission";
dailyevents[13] = "<br />Take a short break";
dailyevents[14] = "<br />Take a short break";
dailyevents[15] = "<br />Revise for math";
dailyevents[16] = "<br />Revise for math";
dailyevents[17] = "<br />Revise for math";
dailyevents[18] = "<br />Revise for math";
dailyevents[19] = "<br />Revise for math";
dailyevents[20] = "<br />Revise for math";
dailyevents[21] = "<br />Revise for math";
dailyevents[22] = "<br />Finish peer-wise assignment + Maths EST";
dailyevents[23] = "<br />Start of holiday";
dailyevents[24] = "";
dailyevents[25] = "";
dailyevents[26] = "";
dailyevents[27] = "";
dailyevents[28] = "";
dailyevents[29] = "";
dailyevents[30] = "";
dailyevents[31] = "";

document.getElementById("calendar").innerHTML = createCalendar(Daytoday);


function createCalendar(calDate) { //function to generate calendar table
    var calendarHTML = "<table id = 'calendar_table' class = 'table-bordered'>"; //initial value of the calendarHTML variable
    calendarHTML += calendarcaption(calDate);
    calendarHTML += rowheading();
    calendarHTML += calDays(calDate);
    calendarHTML += "</table>";
    console.log("running");
    return calendarHTML;
}


function calendarcaption(calDate) {
    var monthName = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    var thisMonth = calDate.getMonth();
    var thisYear = calDate.getFullYear();
    return "<caption>" + "My Schedule For " + monthName[thisMonth] + " " + thisYear + "</caption>";
}

//function to generate the header
function rowheading() {
    //Array of weekly abbreviations
    var dayName = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    var rowHTML = "<tr>"; //opening tag for table row

    for (var i = 0; i < dayName.length; i++) {
        rowHTML += "<th class='calendar_weekdays'>" + dayName[i] + "</th>"; //loop through every item in dayName
    }
    rowHTML += "</tr>"; //add closing tag for table row
    return rowHTML;
}

//calc amt of days in 1 month
function daysInMonth(calDate) {

    var dayCount = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    var thisYear = calDate.getFullYear();
    var thisMonth = calDate.getMonth();

    //leap year error
    if (thisYear % 4 === 0) {
        if ((thisYear % 100 != 0) || (thisYear % 400 === 0)) {
            dayCount[1] = 29;
        }
    }

    return dayCount[thisMonth]; //returns total days in each month

}

function calDays(calDate){
    var day = new Date(calDate.getFullYear(), calDate.getMonth(), 1); //create the first day of the month
    var weekday = day.getDay(); //determines what day month starts on

    var htmlCode = "<tr>"; //initial table row
    for(var i = 0; i < weekday; i++){
        htmlCode += "<td></td>";
    }

    var totalDays = daysInMonth(calDate);
    var today = calDate.getDate();
    for(i = 1; i <= totalDays; i++){ //loop through the total amt of days
        day.setDate(i);
        weekday = day.getDay(); //determine the weekday for each day
        if(weekday === 0) htmlCode += "<tr>"; //new table row on sunday
        if(i === today){
            htmlCode += "<td class = 'calendar_dates' id = 'calendar_today'>" + i + dailyevents[i] + "</td>";
        }
        else{
            htmlCode += "<td class = 'calendar_dates'>" + i + dailyevents[i] + "</td>";
        }
        if(weekday === 6) htmlCode += "</tr>";//saturday, end the table row> 
    }
    return htmlCode; //table row and cells
}