
-- table: employees 
  
 --   | emp_id  |	name   | salary |department_id|	manager_id
 --   |---------|--------|--------|-------------|----------------
 --   |  101	 |  Alice  | 50000	|    1	      |  null
 --   |  102	 |  Bob	   | 75000	|    1	      |  101
 --   |  103	 |  Charlie| 82000	|    2	      |  101
 --   |  104	 |  Diana  | 45000	|    2	      |  103
 --   |  105	 |  Eve	   | 90000	|    1	      |  101
 --   |  106	 |  Frank  | 48000	|    3	      |  103


-- table: departments 

    -- dept_id | dept_name  | budget
    --|------------------------------
    --   1	   |   IT	    | 100000
    --   2	   |   Sales	| 80000
    --   3	   |   HR	    | 60000


-- Find all employees who earn more than the average salary across all employees.
select 
  name,
  salary
from employees 
where salary > (select avg(salary) from employees) 

--  Find the names of all employees who work in departments that have a budget greater than $70,000.
select
  name
from employees 
where department_id in (select dept_id from departments where budget > 70000 )


-- Find all employees who earn more than the average salary of their own department.
select 
  name,
  salary,
  department_id
from employees e1
where salary > ( select avg(salary) from employees e2 where e2.department_id = e1.department_id )
