/*
Section D: Backup a table
1. Write the SQL statement to backup the staff_relation into a new table,
staff_relation_backup.
Section E: Update rows in a table
*/

/*
create table staff_relation_backup(
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
	Designation Varchar(20) Not Null);
*/

-- insert into staff_relation_backup select * from staff_relation;
-- select * from staff_relation;


/*
1. Write the SQL statement to increase permanently the pay of all staff

update
	staff_relation
set
	pay = pay * 1.05
*/

/* 
2. Write the SQL statement to decrease permanently the pay of all staff by $50
and increase permanently the allowance of all staff by 10%

update
	staff_relation
set
	pay = pay - 50,
	allowance = allowance * 1.1;
*/

/*
3. Write the SQL statement to increase permanently by $100 the pay of male full-time staff
who joined before 1996.

update
	staff_relation
set
	pay = pay + 100
where
	Join_Yr < 1996 and Gender = 'm' and Type_of_Employment = 'FT'
*/

/*
Section F: Delete rows from a table
*/ 

/*
1. Write the SQL statement to remove the staff identified by staff number T001.

delete from
	staff_relation
where
	Staff_No = 'T001'
*/
/*
2. Write the SQL statement to remove all the data of the staff relation.

delete from staff_relation
*/
/*
Section G: Restore the table from backup
*/ 
/*
1. Write the SQL statement to restore the staff_relation from staff_relation_backup.

-- insert into staff_relation select * from staff_relation_backup;
*/ 