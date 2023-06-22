use [GroceryStore2222811];

-- 1) Employee relation
INSERT INTO employee_rel (emp_ID, emp_Name, SSN, Phone, StoreRef_ID, Address, PayType, Password, Manager, Email, Date_hired, Date_start, Date_end, Pay)
VALUES
	(1,	'Darrel Philbin', 654269856, 5489659874, 854, '258 Cumberland dr', 0, '1234', 14, 'baldman@gmail.com', NULL, '1985-04-05', '2011-02-02', 20.00),
	(10, 'Jerry Garcia', 758965897, 6521458569, 247, '214 Q st', 1, '1234', 9, 'govperson@gov.gov', NULL, '1990-09-24', NULL, 52000.00),
	(11, 'Lawarnce Tom', 625458569, 9658745632,	159, '2154 Beech st', 0, 'abc', 14,	NULL, NULL, '1969-01-20', '2011-09-01',	15.00),
	(12, 'Dexter Robert', 254125478, 1111111111, 778, '365 Moon dr', 0, 'abc', 15, NULL, NULL, '1990-05-06', NULL, 12.25),
	(13, 'Mark Nick', 563258965, 2225478512, 989, '65412 B St', 0, 'abc', 15, NULL, NULL, '1998-02-05',	NULL, 8.25),
	(14, 'Jeremy David', 111111112, 2356895654,	159, '2 Molly Way', 1, 'abc', 9, NULL, NULL, '2000-06-03', NULL, 16000.00),
	(15, 'Luke Ted', 111111144, 6988532587,	354, '65 Southland Av', 1, NULL, 9, NULL, NULL, '2004-09-09', NULL, 20000.00),
	(2,	'Ricky Tanner',	125651452, 9856984523,	696, '1585 H st', 0, 'abc', 4, 'omegaman@aol.com', NULL, '1990-06-08', '1999-06-10', 10.00),
	(3,	'Susan Phillips', 145969658, 2586521452, 369, '695 LMNOP st', 0, 'Password', 4, 'streetsmartkid@hampster.edu', NULL, '1972-06-09', NULL, 15.00),
	(4,	'George Scott',	147589652, 5896583541,	696, '4521 Gold st', 1, 'Alpha', 9, NULL, NULL, '1999-07-25', NULL, 42000.00),
	(5,	'Erin Abernathy', 256985698, 4736593569, 369, '635 Number ln', 0, 'Bottle', 6, 'drinkerster@gmail.com',	NULL, '1998-12-20', NULL, 30.00),
	(6, 'Ted Smith', 352956587,	2586584763,	369, '12 S st',	1, 'Worksu...', 9, NULL, NULL, '1989-06-08', NULL, 50000.00),
	(7,	'Harry Buts', 458521658, 2586584763, 674, '1 wonder st', 0,	'Password',	6,	NULL, NULL, '1970-10-20',	NULL, 12.00),
	(8,	'Maynar Teener', 256656521,	2596573257,	674, '24 nice ln', 0, 'Password', 6, 'Meme585@gmail.com', NULL, '2005-06-04', NULL, 9.25),
	(9,	'Matt Longfella', 958786548, 5249868525, 354, '6144 Computer Street', 1, 'Password', NULL, 'thisisshort@az.com', NULL, '2000-09-24', NULL, 60000.00);

-- 2) Customer relation
INSERT INTO customer_rel (cust_ID, cust_Name, cust_Phone, cust_Email, DateCreated, DateLastTrans)
VALUES
	(105, 'Master Shake',	5555555555, 'MixMaster@crimefighter.org', '8/25/2005', '8/18/2011'),
	(178, 'Bruce Wayne',	6619872145,	'IamBatman@crimefighter.org', '1/1/2004', '2/15/2011'),
	(179, 'Seymoure Butes',	4789582145,	'butes@education.edu', '5/15/2011', '8/18/2011'),
	(50, 'Bob Hope',	6615552485,	'Bobhope@gmail.com', '1/1/2001', '5/7/2011'),
	(51, 'Renee Hicks',	4589854588,	'Dragonthing@aol.com', '4/8/2005', '4/25/2011'),
	(52, 'Scott Sheer',	4176521425,	'Scotts@hotmail.com', '2/19/2011', '3/14/2011'),
	(53, 'Colleen Mctyre',	NULL, 'CMcT@ct.com', '8/12/2008', '12/5/2009'),
	(58, 'Bart Simpson', NULL,	NULL, '6/6/2001', '8/25/2007'),
	(67, 'Lisa Girl', 6619755896, NULL,	'1/4/1999', '4/6/2011'),
	(99, 'Jeremy Scott', 4586895847, 'TheBigMan@gmail.com', '8/9/2001',	'10/10/2001');

-- 3) Store relation
INSERT INTO store_rel (store_id, store_address, manager_id)
VALUES
	(159, '13636 Fir St', 14),
	(247, '650 Beech St',10),
	(348, '120 Acacia Way', 10), 
	(354, '820 Birch Rd', 15),
	(369, '940 Green St', 6),
	(674, '14496 Maple Way', 6),
	(696, '710 Edison Dr', 4),
	(778, '341 Main St', 15),
	(854, '22566 Elm St', 14),
	(989, '617 Oak St', 15);

-- 4) Item relation

INSERT INTO item_rel(item_id, Brand, Description, Price, Cost, Shape, Size, UPC, Weight, Taxable)
VALUES
	(12, 'N bisco',	'Cookies', 2.25, 1.00, 'Oval', '23x5x20', 224852, 22.40, 1),
	(145, 'Kleenex', 'Tissues', 2.99, 1.00,	'Rectangle', '3x19x4', 178965, 34.00, 0),
	(1566, 'HomeBrand', 'Spaghetti', 0.99, 0.50, 'Round', '3x3x3', 698547, 3.00, 0),
	(2365, 'Kellogg', 'Cereal',	1.99, 0.50, 'Round', '10x10x10', 557858, 18.00,	1),
	(256, 'Hersey',	'Candy', 3.99, 2.00, 'Rectangle', '4x16x6', 123058,	52.80, 0),
	(335, 'DelMonte', 'Canned Fruit', 0.50,	0.10, 'Square', '3x3x3', 411255, 5.20, 1),
	(3521, 'Nabisco', 'Crackers', 4.00,	2.00, 'Round', '4x4x4', 254413,	2.00, 0),
	(4587, 'Kraft', 'Cheese', 6.00,	4.00, 'Rectangle', '6x12x3', 845532, 0.11, 0),
	(658, 'PhilipMorris', 'Cigarettes',	5.00, 3.00,	'Square', '8x8x8', 596543, 89.00, 0),
	(84854, 'Quaker', 'Oatmeal', 2.50, 1.00, 'Square', '2x2x2', 556487,	1.00, 0);

-- 5) Inventory relation
INSERT INTO inventory_rel(store_id, item_id, quantity)
VALUES
	(159, 1566, 31),
	(159, 335, 27),
	(247, 145, 56),
	(348, 256, 100), 
	(354, 1566, 4),
	(369, 3521, 113),
	(696, 658, 38),
	(674, 2365, 0),
	(674, 4587, 23),
	(696, 12, 23),
	(778, 84854, 350),
	(854, 12, 10),
	(854, 658, 10),
	(989, 145, 560);




-- 6) Transaction Rel
INSERT INTO transaction_rel(transaction_id, emp_id, dateTrans, cust_id, store_id) 
VALUES
	(1, 10, '2011-06-10', 50, 854),
	(2, 12, '2011-11-12', 178, 778),
	(3, 11,	'2010-06-05', 99, 159),
	(4, 3, '2007-04-05', 105, 369),
	(5, 15, '2011-06-09', 51, 354),
	(6, 2, '2010-08-12',52, 696),
	(7, 7, '2009-11-05', 179, 674)



-- 7) Basket relation
INSERT INTO basket_rel(transaction_id, Item_id, Quantity)
VALUES
	(1, 256, 2),
	(1, 2365, 2),
	(2, 145, 10),
	(3, 4587, 2),
	(4, 4587, 4),
	(5, 2566, 4),
	(5, 145, 3),
	(5, 3521, 2),
	(5, 84854, 2),
	(6, 2365, 2),
	(6, 4587, 2),
	(7, 12, 2),
	(7, 658, 2)

