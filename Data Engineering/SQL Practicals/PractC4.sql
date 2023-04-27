/*
Section A: Multiple search conditions using AND operator
*/
select * from staff_relation
/*
1. Write the SQL statement to list the citizenship and staff names all foreign staff from the
School of Digital Media and Infocomm Technology (DMIT). Sort the result in ascending order
of staff name within descending order of citizenship.

SELECT
	citizenship, staff_name
FROM
	staff_relation
WHERE
	dept_cd = 'DMIT' and citizenship != 'Singapore'
ORDER BY
	citizenship desc, staff_name
*/
/*
2. Write the SQL statement to list in ascending order, the staff name of all male staff who are
Singapore citizens born in the sixties (from 1960 to 1969 inclusive). Re-label staff name
column’s header as ‘Singaporean Men’.

SELECT 
	staff_name as "Singaporean Men"
FROM
	staff_relation
WHERE
	Citizenship = 'Singapore' 
	AND 
	Gender = 'M' 
	AND 
	Date_Of_Birth BETWEEN '1960' AND '1969'
ORDER BY
	staff_name
*/
/*
Section B: Multiple search conditions using OR operator
*/
/*
1. Write the SQL statement to list the marital status and staff name of staff that are divorced
or widowed. (use the OR operator first then use the IN operator)

SELECT 
	marital_status, staff_name 
FROM 
	staff_relation
WHERE 
	(marital_status = 'D') OR (marital_status = 'W')

SELECT 
	marital_status, staff_name 
FROM 
	staff_relation
WHERE 
	marital_status in ('D', 'W')
*/
/*
2. Write the SQL statement to list the highest qualification and staff name of staff who are
bachelor degree holders or whose names have the letter n. Sort the result in ascending
order of staff name within ascending order of highest qualification.

SELECT 
	highest_qln, staff_name
FROM 
	staff_relation
WHERE
	highest_qln LIKE 'B%' or staff_name LIKE '%n%'
ORDER BY
	2,1
*/
/*
Section C: Multiple search conditions using AND & OR operators
*/
/*
1. Write the SQL statement to list the marital status and staff name of female staff that are
divorced or widowed. (Use the OR operator first then use the IN operator. Remember to
use parentheses to encapsulate two conditions as one for OR. )

SELECT 
	marital_status, staff_name
FROM
	staff_relation
WHERE 
	marital_status in ('D','W') AND gender = 'F'
*/
/*
Section D: Parentheses within Parentheses
*/
/*
1. Write the SQL statement to list the gender, pay, and staff name of staff who are receiving
pay. List the female staff who are paid between 4000 and 7000 or the male staff who are
paid between 2000 and 6000. Sort in ascending order of pay within ascending order of
gender.	
*/
SELECT 
	gender, pay, staff_name
FROM
	staff_relation
WHERE
	pay is not null AND
	((gender = 'F' and pay between 4000 and 7000) OR 
	(gender = 'M' and pay between 2000 and 6000))	
ORDER BY 
	gender, pay
/*
2. List the staff number, name, gender, date of birth, pay, grade and join year of female staff
who are not in grade ‘SSD’ or ‘SSE’ but are either born before 1963 or whose pay is more
than $6,000 or joined between 1997 and 2000.
*/
SELECT 
	staff_no, staff_name, gender, Date_Of_Birth, pay, grade,join_yr
FROM
	staff_relation
WHERE
	gender = 'F' and
	grade not in ('SSE', 'SSD') and 
	(year(Date_Of_Birth) < 1963 or pay > 6000 or Join_Yr between 1997 and 2000)