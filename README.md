# Github and local project, virtual environment, install necessary packages
## Terminal Commands:
```
python -m venv .venv
.\.venv\Scripts\activate
```

## install the package needed panda , pyarrow 
```
python -m pip install pandas pyarrow
```

## freezed the requirments 
```
python -m pip freeze > requirements.txt
```

## added the SQL files to the project 
```
testSql.Py script to run all the sql script to connect to DB and create table and do CRUD functionality .
```

# SQL related operations in python, and perform CRUD operations
## Establish connection using sqlite3
```
sqlite3.connect(db_filepath) 
```

## Create Table using sqlite3
```

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

```

##  Insert data into a table
```
INSERT INTO department
(department_id,
department_name)
VALUES
(1,
"HR");
INSERT INTO department
(department_id,
department_name)
VALUES
(2,
"IT");
INSERT INTO department
(department_id,
department_name)
VALUES
(3,
"Finance");
INSERT INTO employee
(employee_id,
employee_name,
department_id)
VALUES
(101,"John", 1);
```
## Read data from a table
```
select * from department;
```

## Update table
```
update employee set employee_name = "Kamalini" where employee_id = "1"
```

## Delete data from a Table
```
Delete from employee where department_id = 3 
Delete from department where department_id = 3 
```

# Advanced operations on tables
## Join two tables
```
select department.department_name, employee.employee_id, employee.employee_name from department join employee on department.department_id= employee.department_id 

```
## Group by operation
```
select department_id , count(employee_id) from employee group by department_id
```

