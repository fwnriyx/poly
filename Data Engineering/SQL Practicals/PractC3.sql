/*
1. Write two different SQL statements to display all columns and all rows of the Staff relation

SELECT * from staff_relation
or u can list out all the columns
*/


/*
2.Write the SQL statement to list the citizenship of all staff. Display the results in descending
order of citizenship

select 
	citizenship
from 
	staff_relation
order by 
	citizenship desc
*/

/*
3. Write the SQL statement to list different citizenships of the staff. Do not display duplicate
citizenship

select 
	distinct citizenship
from 
	staff_relation
*/

/*
4. Write the SQL statement to list the staff name and date of birth of all staff. Rename the
staff name column as ‘Name of Staff’ using the AS keyword and date of birth as Date-of-Birth 
without using the AS keyword when specifying column aliases. Display the results from oldest to youngest staff.
select 
	staff_name as 'Name of Staff', 
	Date_Of_Birth as 'Date of Birth'
from 
	staff_relation
order by 
	Date_Of_Birth
*/

/*
5. Write the SQL statement to display all columns of all departments, sorted in descending order
of department code. You must use column number instead of column name in the order by
clause.

SELECT * FROM department_relation order by 1 desc
*/

/*
6. Write the SQL statement to list the department code and staff name of all staff. First, sort the
result in descending order of department code. For staff working in the same department,
display the results in descending order of staff name.

SELECT 
	dept_cd, staff_name
FROM
	staff_relation
ORDER BY 
	dept_cd desc, staff_name
*/

/*
7. Write the SQL statement to list department name and head of department start date of all
departments. Re-label the list department name as Department_Name and head of
department start date as HOD_ Appointment_Date.

SELECT 
	Dept_cd, Dept_Name as 'Department_Name', HOD_Appt_Date as 'HOD_Appointment_Date'
FROM
	department_relation

*/

/* 8. Write the SQL statement to display all columns (using the wild card *) and all rows/ of the
department_relation. Sort the result in descending order of the staff number in each
department. You must use column number instead of column name in the order by clause.

SELECT 
	*
FROM 
	department_relation
ORDER BY
	4 DESC
*/                                       