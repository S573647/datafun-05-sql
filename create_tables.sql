
CREATE TABLE IF NOT EXISTS department (
  department_id int NOT NULL DEFAULT '0' PRIMARY KEY ,
  department_name varchar(100) NOT NULL   
);
    
CREATE TABLE IF NOT EXISTS employee (
employee_id int NOT NULL DEFAULT '0' PRIMARY KEY,
employee_name varchar(100) NOT NULL,
department_id int DEFAULT NULL,  
FOREIGN KEY (department_id) REFERENCES department (department_id)
);
