use [Grocerystore2222811];
--SELECT * FROM employee_rel

	/* i) Write a query to show the name of customer, the date of transaction made by
	the customer, the store where the transaction takes place, its manager’s name,
	the item brand, description and quantity purchased for the transaction and the
	employee who serves the transaction. A sample output should be as shown
	below. 

	SELECT 
		c.cust_Name AS 'custName',
		s.store_id AS Store_ID,
		s.store_address AS 'Store Address',
		e.emp_Name AS 'Manager of the Store',
		dateTrans AS 'Transaction Date',
		i.brand AS 'Brand',
		i.description AS 'Description',
		b.Quantity AS 'Quantity Purchased',
		eid.emp_Name AS 'Served By'
	FROM
		transaction_rel t
		INNER JOIN customer_rel c ON t.cust_id = c.cust_ID
		INNER JOIN store_rel s ON t.store_id = s.store_id
		INNER JOIN employee_rel e ON s.manager_id = e.emp_ID
		INNER JOIN basket_rel b ON t.transaction_id = b.transaction_id
		INNER JOIN item_rel i ON b.Item_id = i.item_ID
		INNER JOIN employee_rel eid ON t.emp_id = eid.emp_ID;
*/

/* ii) Write a query to show the following store details and their item inventories.

SELECT 
	s.manager_id, e.emp_Name, i.store_id, i.item_id, i.quantity 
FROM 
	inventory_rel i
INNER JOIN 
	store_rel s on s.store_id = i.store_id
INNER JOIN
	employee_rel e on e.emp_ID = s.manager_id
ORDER BY
	i.store_id ASC
*/

/* 
iii) To list all customers who bought not more than 2 items on any single transaction:
SELECT 
	c.Cust_ID, c.cust_Name
FROM 
	customer_rel c 
INNER JOIN 
	transaction_rel t ON c.Cust_ID = t.cust_id
INNER JOIN
	basket_rel b ON t.transaction_id = b.transaction_id
GROUP BY
	c.cust_ID, c.cust_Name
HAVING	
	MAX(b.Quantity) <= 2
*/


/*
iv) To show the item_ID, its description, total amount ‘Retail’, based on Price and total amount based on cost ‘Wholesale’ 
for those items which are kept by at least 2 stores:
SELECT 
	it.item_ID, it.Description, SUM(it.Price * i.Quantity) AS Retail, SUM(it.Cost * i.Quantity) AS Wholesale 
FROM 
	item_rel it
INNER JOIN 
	inventory_rel i ON it.Item_ID = i.Item_ID
GROUP BY 
	it.Item_ID, it.Description
HAVING 
	COUNT(DISTINCT i.Store_ID) >= 2;
*/

/*
v) To show the ID and name of employees and the ID and names their managers:
SELECT 
	e.emp_ID as 'Store Manage ID', e.emp_Name as 'Name of Staff', m.emp_ID AS 'Store Managed', m.emp_Name AS 'manager_name'
FROM 
	employee_rel e
INNER JOIN 
	employee_rel m ON e.Manager = m.emp_ID
*/

/*
vi) Write a query to list the emp_ID, name of manager and the boss’ ID and name together with the store_ID and its address where both the manager and the 
boss are stationed at the same store. 

select 
	e.emp_Name AS 'Manager Name', e.Manager AS 'Boss ID', e.Manager AS 'Manager ID', em.emp_Name AS 'Boss Name',e.StoreRef_ID, em.Address, s.store_address
from 
	employee_rel e
JOIN 
	employee_rel em ON e.Manager = em.emp_ID
JOIN 
	store_rel s ON em.StoreRef_ID = s.Store_ID
WHERE 
	e.PayType = 1 and e.StoreRef_ID = em.StoreRef_ID
*/