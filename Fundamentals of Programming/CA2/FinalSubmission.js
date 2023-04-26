// Name : Muhammad Fitri Amir bin Abdullah
// Class: DCITP/1A/08
// Adm : 2222811
// Used for staff in XYZ company to see the members in the XYZ membership program.Gives users 4 options, displays members details, and exits the program.

var input = require('readline-sync');

class Member {
    constructor(Name, MembershipClass, DateJoined, DateOfBirth, PointsEarned) {
        this.Name = Name;
        this.MembershipClass = MembershipClass;
        this.DateJoined = DateJoined;
        this.DateOfBirth = DateOfBirth;
        this.PointsEarned = PointsEarned;
    }
}

const memberArr = [
    new Member("Leonardo", "Gold", "1 Dec 2019", "1 Jan 1980", 1400),
    new Member("Catherine", "Ruby", "14 Jan 2020", "28 Oct 1985", 250),
    new Member("Luther", "Gold", "29 Apr 2020", "16 Mar 1992", 3350),
    new Member("Bruce", "Diamond", "3 Jun 2020", "18 Mar 1994", 40200),
    new Member("Amy", "Gold", "5 Jun 2020", "31 May 2000", 500)
]


class memberGroup {
    constructor(tMembers) {
        this.tMembers = tMembers;
    }

    memberList = [
        new Member("Leonardo", "Gold", "1 Dec 2019", "1 Jan 1980", 1400),
        new Member("Catherine", "Ruby", "14 Jan 2020", "28 Oct 1985", 250),
        new Member("Luther", "Gold", "29 Apr 2020", "16 Mar 1992", 3350),
        new Member("Bruce", "Diamond", "3 Jun 2020", "18 Mar 1994", 40200),
        new Member("Amy", "Gold", "5 Jun 2020", "31 May 2000", 500)
    ];

    addMember() {
        //Pushes new member into the back of the member list
        let newMember = new Member(newName, "Ruby", tdy, newDOB, 0);
        this.tMembers.push(newMember);
        return newMember;
    }
    memberListLength() {
        //fetches the length of tMembers
        return this.tMembers.length;
    }
    get members() {
        return this.tMembers;
    }
    searchMembers(searchName) {
        //initialises a new variable called main, changes depending on result.
        var status;
        var main = null;
        for (let i = 0; i < this.tMembers.length; i++) {
            if (searchName == (this.tMembers[i].Name)) {
                main = "\n\n\tName: " + members.tMembers[i].Name + "\n\tMembership Type: " + members.tMembers[i].MembershipClass + "\n\tDate joined: " + members.tMembers[i].DateJoined +
                    "\n\tDate of birth: " + members.tMembers[i].DateOfBirth + "\n\tPoints earned: " + members.tMembers[i].PointsEarned + "\n"
                status = true;
                break;
            }
            else {
                main = "Member does not exist"
                status = false;
            }
        }
        return main;
    }
    notInList(newName) {
        //Validates if the name of the new member matches any of the names in the current list.
        var nameIn = null;
        for (let i = 0; i < this.tMembers.length; i++) {
            if (newName == (this.tMembers[i].Name)) {
                nameIn = "";
                break;
            }
            else {
                nameIn = null;
                break;
            }
        }
        return nameIn
    }
    pointsChecker(){
        var lowestP = members.tMembers[0].Name;
        var highestP = members.tMembers[0].Name;
        var storeP = members.tMembers[0].PointsEarned;
        for(i = 0; i < this.memberListLength(); i++){
            if(members.tMembers[i].PointsEarned > storeP) {
                console.log(members.tMembers[i].Name);
                storeP = members.tMembers[i].PointsEarned;
                highestP = members.tMembers[i].Name;
            }
            else if(members.tMembers[i].PointsEarned < storeP){
                console.log(members.tMembers[i].Name);
                storeP = members.tMembers[i].PointsEarned;
                lowestP = members.tMembers[i].Name;
                break;
            }
        }
        console.log("\n\t\tLowest member: " + lowestP + "\n\t\tHighest member  : " + highestP);
    }
    addPoints(amSpent) {
        for (let i = 0; i < this.tMembers.length; i++) {
            if (searchName == (this.tMembers[i].Name)) {
                if (amSpent <= 50.01) {
                    members.tMembers[i].PointsEarned += 10;
                }
                else if (amSpent <= 100.01) {
                    members.tMembers[i].PointsEarned += 50;
                }
                else if (amSpent <= 200.01) {
                    members.tMembers[i].PointsEarned += 100;
                }
                else if (amSpent <= 500.01) {
                    members.tMembers[i].PointsEarned += 200;
                }
                else if (amSpent <= 1000.01) {
                    members.tMembers[i].PointsEarned += 500;
                }
                else if (amSpent <= 2500.01) {
                    members.tMembers[i].PointsEarned += 1000;
                }
                else if (amSpent > 2500.01) {
                    members.tMembers[i].PointsEarned += 2000;
                }
                else {
                    console.log("Enter a valid amount.");
                }
                for ( i = 0; i < this.tMembers.length; i++) {
                    if (members.tMembers[i].PointsEarned >= 20000) {
                        members.tMembers[i].MembershipClass = "Diamond";
                    }
                    else if (members.tMembers[i].PointsEarned >= 5000) {
                        members.tMembers[i].MembershipClass = "Platinum"
                    }
                    else if (members.tMembers[i].PointsEarned >= 500) {
                        members.tMembers[i].MembershipClass = "Gold"
                    }
                    else if(members.tMembers[i].PointsEarned < 500) {
                        members.tMembers[i].MembershipClass = "Ruby"
                    }
                }
            }
            }
        
    }
}   
function disMemberInfo(index) {
    //Displays the information of different members based on the index.
    console.log("\n\tName: " + members.tMembers[index].Name +
        "\n\tMembership Type: " + members.tMembers[index].MembershipClass + "\n\t" +
        "Date joined: " + members.tMembers[index].DateJoined +
        "\n\tDate of birth: " + members.tMembers[index].DateOfBirth +
        "\n\tPoints earned: " + members.tMembers[index].PointsEarned + "\n\n");
}


const d = new Date();
d.getDate();
const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

const m = new Date();
let month = months[m.getMonth()];

const y = new Date();
y.getFullYear();

const tdy = d.getDate() + " " + month + " " + y.getFullYear();

//Brings tMembers into a new variable called members, easier to instanciate. 
var members = new memberGroup(memberArr);

console.log("Welcome to XYZ Membership Loyalty Programme!");


var name = input.question("Please enter your name: ");

do {
    var choice = input.question("\nHi " + name + " , please select your choice:" +
        "\n1. Display all members' information\n" +
        "2. Display member information\n" +
        "3. Add new member\n" +
        "4. Update points earned\n" +
        "5. Statistics\n" +
        "6. Exit\n>> ");
    if (choice != "1" && choice != "2" && choice != "3" && choice != "4" && choice != "5" && choice != "6") {
        //when a value that isnt a number is inputted, the user will be asked to state choice again.
        console.log("Please enter a valid input.\n");
    }
    else if (choice == 1) {
        //uses array indexes to match the different data of the members
        for (let i = 0; i < members.memberListLength(); i++)
            disMemberInfo(i)

    }
    else if (choice == "2") {
        var searchName = input.question("\n\tPlease enter member's name: ");
        //As main is returned, the console log will display the result of main.
        console.log(members.searchMembers(searchName));
    }
    else if (choice == "3") {
        var newName = input.question("\n\tPlease enter member's name: ");
        var newDOB = input.question("\tPlease enter member's date of birth: ");
        // After prompting for member's info, puts it into an array and adds it into tMembers.
        members.notInList(newName);
        members.addMember(newName, newDOB);
    }
    else if (choice == "4") {
        var searchName = input.question("\n\tPlease enter member's name: ");
        for (let i = 0; i < members.memberListLength(); i++) {
            if (searchName == members.tMembers[i].Name) {
                var amSpent = parseInt(input.question("\tPlease enter amount spent: $"));
                members.addPoints(amSpent);
            }
        }
    }

    else if (choice == "5") {
        var choiceFive = input.question("\n\tPlease select an option from the sub-menu: \n\t" +
            "1. Display names of (all) a certain type of members only.\n\t" +
            "2. Display the name of the youngest and oldest members in the system\n\t" +
            "3. Display the names of members with the highest and lowest points earned.\n\t" +
            "4. Display total number of members in each membership type.\n\t" +
            "5. Display the total points in each membership type.\n\t" +
            "6. Return to main menu.\n\t>> ");
        do {
            if (choiceFive != "1" && choice != "2" && choice != "3" && choice != "4" && choice != "5" && choice != "6") {
                console.log("Please enter a valid input");
            }
            if (choiceFive == "1") {
                var status = "";
                //empty array to store all members that have the same type
                var sameClass = [];
                var memType = input.question("\nEnter membership type: ");
                for (var i = 0; i < members.memberListLength(); i++) {
                    if (memType == members.tMembers[i].MembershipClass) {
                        sameClass.push(members.tMembers[i].Name);
                        status = "\n\tMembership of class type: " + sameClass + "\n";
                    }
                    else if (memType != "Ruby" && memType != "Platinum" && memType != "Diamond" && memType != "Gold") {
                        status = "Please enter a valid membership type.\n"
                    }
                }
                console.log(status);
                break;
            }
            if (choiceFive == "2") {
                // empty array to store all age of members
                var ageArr = [];
                for(i = 0 ; i < members.memberListLength() ; i++){
                    //converts age of members into milliseconds in order to compare
                    ageArr.push((Date.parse(members.tMembers[i].DateOfBirth)))
                }
                //initialises the oldest and youngest member to be the first member in order to start comparisons
                var oldest = members.tMembers[0].Name
                var youngest = members.tMembers[0].Name
                var storeage1 = ageArr[0]
                for(i = 0; i < ageArr.length; i++){
                    if(ageArr[i] < storeage1){
                        storeage1 = ageArr[i]
                        oldest = members.tMembers[i].Name
                    }
                    else if(ageArr[i] > storeage1){
                        storeage1 = ageArr[i]
                        youngest = members.tMembers[i].Name
                    }
                }
                console.log("\n\t\tYoungest member: " + youngest + "\n\t\tOldest member  : " + oldest)
                break;
            }
            if (choiceFive == "3") {
                // console.log(members.largestNumber());
                // console.log(members.smallestNumber());
                members.pointsChecker();
                break;
            }
            if (choiceFive == "4") {
                //Create 4 new arrays for the list of all the members in all 4 classes
                var rubyList = [];
                var diamondList = [];
                var platinumList = [];
                var goldList = [];
                for (let i = 0; i < members.memberListLength(); i++) {
                    if (members.tMembers[i].MembershipClass == "Ruby") {
                        rubyList.push(members.tMembers[i].Name);
                    }
                    if (members.tMembers[i].MembershipClass == "Diamond") {
                        diamondList.push(members.tMembers[i].Name);
                    }
                    if (members.tMembers[i].MembershipClass == "Platinum") {
                        platinumList.push(members.tMembers[i].Name);
                    }
                    if (members.tMembers[i].MembershipClass == "Gold") {
                        goldList.push(members.tMembers[i].Name);
                    }
                }
                console.log("\n\t\tRuby: " + rubyList.length +
                    "\n\t\tDiamond: " + diamondList.length +
                    "\n\t\tPlatinum: " + platinumList.length +
                    "\n\t\tGold: " + goldList.length);
                break;
            }
            if (choiceFive == "5") {
                // 4 different variables to store the different amount of points available in the different ranks
                var totalRuby = 0;
                var totalPlat = 0;
                var totalGold = 0;
                var totalDia = 0;
                for (let i = 0; i < members.memberListLength(); i++) {
                    switch (members.tMembers[i].MembershipClass) {
                        case ("Ruby"):
                            totalRuby += members.tMembers[i].PointsEarned;
                            break;
                        case ("Platinum"):
                            totalPlat += members.tMembers[i].PointsEarned;
                            break;
                        case ("Gold"):
                            totalGold += members.tMembers[i].PointsEarned;
                            break;
                        case ("Diamond"):
                            totalDia += members.tMembers[i].PointsEarned;
                            break;
                    }
                }
                console.log("Ruby: " + totalRuby +
                    "\nGold: " + totalGold +
                    "\nPlatinum: " + totalPlat +
                    "\nDiamond: " + totalDia);
                break;
            }
        }
        while (choiceFive != "6")
    }
    else {
        console.log("Thank you & goodbye!\n");
    }
} while (choice != "6") //loops as long as choice isnt 4
