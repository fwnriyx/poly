--CREATE DATABASE [GroceryStore2222811];
use [GroceryStore2222811];


-- 1) Create Employee relation, store all employee data

CREATE TABLE employee_rel (
  emp_ID INT PRIMARY KEY,
  emp_Name VARCHAR(50) NOT NULL,
  SSN INT NOT NULL,
  Phone BIGINT NOT NULL,
  StoreRef_ID INT NOT NULL,
  Address VARCHAR(100) NOT NULL,
  PayType INT NOT NULL,
  Password VARCHAR(50) NULL,
  Manager INT NULL,
  Email VARCHAR(100) NULL,
  Date_hired DATE NULL,
  Date_start DATE NOT NULL,
  Date_end DATE NULL,
  Pay DECIMAL(7,2) NOT NULL
);

 --2) customer_relation
 --Purpose: record all customer info in a table

CREATE TABLE customer_rel (
    cust_ID INT PRIMARY KEY,
    cust_Name VARCHAR(50) NOT NULL,
    cust_Phone BIGINT NULL,
    cust_Email VARCHAR(50) NULL,
    DateCreated DATE NOT NULL,
	  DateLastTrans DATE NOT NULL
);

-- 3) store_relation
-- Purpose: record all stores and their location/address as well as the manager that manages

CREATE TABLE store_rel (
	store_id INT PRIMARY KEY,
	store_address VARCHAR(200) NOT NULL,
	manager_id INT NOT NULL
);

-- 4) item_relation
-- Purpose: assign unique identifier for each UNIQUE ITEM the company has and the info of every item

CREATE TABLE item_rel (
  item_id INT PRIMARY KEY,
  brand VARCHAR(50) NOT NULL,
  description VARCHAR(200) NOT NULL,
  price DECIMAL(7, 2) NOT NULL,
  cost DECIMAL(7, 2) NOT NULL,
  shape VARCHAR(20) NOT NULL,
  size VARCHAR(20) NOT NULL,
  UPC INT NOT NULL,
  Weight DECIMAL(7, 2) NOT NULL,
  Taxable BIT NOT NULL
);

-- 5) inventory_relation
-- Purpose: record assigned count of each item to each store

CREATE TABLE inventory_rel (
	quantity INT NOT NULL, 
	item_id INT NOT NULL,
	store_id INT NOT NULL,

	primary key (item_id, store_id)	
);

-- 6) transaction_relation
-- Purpose: record all transactions made by customers at different stores in a table

CREATE TABLE transaction_rel (
	transaction_id INT PRIMARY KEY,
	emp_id INT NOT NULL,
	dateTrans DATE NOT NULL,
    cust_id INT NOT NULL, 
	store_id INT NOT NULL
);

-- 7) basket_relation
-- Purpose: find out the different items and the quantities before they complete their transaction
CREATE TABLE basket_rel (
	transaction_id INT NOT NULL,
	item_id INT NOT NULL,
	quantity INT NOT NULL
	primary key (transaction_id, item_id)
);



ALTER TABLE inventory_rel
ADD FOREIGN KEY (store_id) REFERENCES store_rel(store_id);

ALTER TABLE inventory_rel
ADD FOREIGN KEY (item_id) REFERENCES item_rel(item_id)

ALTER TABLE transaction_rel
ADD FOREIGN KEY (cust_id) REFERENCES customer_rel(cust_id)

ALTER TABLE transaction_rel
ADD FOREIGN KEY (store_id) REFERENCES store_rel(store_id)

ALTER TABLE transaction_rel
ADD FOREIGN KEY (emp_id) REFERENCES employee_rel(emp_id)

ALTER TABLE basket_rel
ADD FOREIGN KEY (transaction_id) REFERENCES transaction_rel(transaction_id)