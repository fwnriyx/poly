use [Royal_Poly_DB];

-- Create a new Database

-- Create Database Royal_Poly_DB

-- Create staff_relation table

 /*	create table staff_relation(
	Staff_No Char (4) primary key,
	Staff_Name Varchar(100) Not Null,
	Supervisor Char(4) Null,
	Date_Of_Birth Date Not Null,
	Grade VarChar(5) Not Null,
	Marital_Status Char(1) Not Null,
	Pay Decimal(7,2) Null,
	Allowance Decimal(7,2) Null,
	Hourly_Rate Decimal(7,2) Null,
	Gender Char(1) Not Null,
	Citizenship Varchar(10) Not Null,
	Join_Yr Integer Not Null,
	Dept_Cd VarChar(5) Not Null,
	Type_of_Employment Char(2) Not Null,
	Highest_Qln Varchar(10) Not Null,
	Designation Varchar(20) Not Null
	);
*/
-- select * from staff_relation

/*	create table course_relation(
	Crse_Cd VarChar(5) primary key,
	Crse_Name VarChar(100) Not Null,
	Offered_By Varchar(5) Not Null,
	Crse_Fee Decimal(7,2) Not Null,
	Lab_Fee Decimal(7,2) Null
	);
*/

-- To check the content of a table use a query
	select * from course_relation

/*	create table department_relation(
	Dept_Cd VarChar(5) primary key,
	Dept_Name VarChar(100) Not Null,
	HOD Char(4) Not Null,
	No_Of_Staff Integer Null,
	Max_Staff_Strength Integer Null,
	Budget Decimal(9,2) Null,
	Expenditure Decimal(9,2) Null,
	HOD_Appt_Date Date Null
);
*/

-- select * from department_relation