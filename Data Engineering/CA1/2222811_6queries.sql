use [Grocery_Store_DB];

/* i) Write a query to show the name of customer, the date of transaction made by
the customer, the store where the transaction takes place, its manager’s name,
the item brand, description and quantity purchased for the transaction and the
employee who serves the transaction. A sample output should be as shown
below. 

SELECT
	custName, transDate, storeID, storeManager, i.brand, i.info, i.quantity, empServed
FROM 
	storeDB 
INNER JOIN
	itemDB 
ON 
	s.brand =  i.brand;
ORDER BY
	custName 
*/

/* ii) Write a query to show the following store details and their item inventories.*/

SELECT  * FROM itemDB 

