-- Populating table
use [Royal_Poly_DB];

--Courses w/o lab fee
/*
insert into 
 course_relation (crse_cd, crse_name, offered_by, crse_fee)
values
 ('DBA','Diploma in Business Administration','SB',500.00),
 ('DFI','Diploma in Financial Informatics','SB',800.00)
 */

-- Courses w lab fee
/*
insert into 
 course_relation
values
 ('DBIT','Diploma in Business and Information Technology','DMIT',700.00,100.00),
 ('DDM','Diploma in Digital Media','DMIT',1000.00,900.00),
 ('DISM','Diploma in Infocomm Security Management','DMIT',900.00,300.00),
 ('DIT','Diploma in Information Technology','DMIT',650.00,450.00)
 */

--Clear table
-- delete from course_relation;

 /*
 -- alt method
insert into 
 course_relation
values
 ('DBA','Diploma in Business Administration','SB',500.00,NULL),
 ('DFI','Diploma in Financial Informatics','SB',800.00,NULL),
 ('DBIT','Diploma in Business and Information Technology','DMIT',700.00,100.00),
 ('DDM','Diploma in Digital Media','DMIT',1000.00,900.00),
 ('DISM','Diploma in Infocomm Security Management','DMIT',900.00,300.00),
 ('DIT','Diploma in Information Technology','DMIT',650.00,450.00)
 */

--select * from course_relation

/*
insert into 
 department_relation
values
 ('DMIT','School of Digital Media and Infocomm Technology','S001',82,92,90000.00,45000.00,'2009-04-01'), 
 ('DPO','Deputy Principal''s Office','T002',3,3,6000.00,NULL,NULL),
 ('PO','Principal''s Office','T001',4,4,7500.00,NULL,'2008-01-01'), 
 ('SB','School of Business','S006',8,90,80000.00,88000.00,'1996-10-01') 
*/

select * from department_relation;
select * from course_relation;
select * from staff_relation