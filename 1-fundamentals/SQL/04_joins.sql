-- ===============================================================
-- Author: Nigina Irgasheva
-- Date: 2025-10-20
-- Topic: Cross Join, Full Outer Join , Self Join
-- Task: Restaurant Menu Combinations
/*
    1. Create all possible meal combinations (main course + drink)
    2. Count how many total combinations exist
    3. List only combinations where main course is "Pizza"
*/
-- Tables:
--    MainCourses:
--    | id | main_course |
--    |----|-------------|
--    | 1  | Burger      |
--    | 2  | Pizza       |
--    | 3  | Pasta       |
    
--    Drinks:
--    | id | drink    |
--    |----|----------|
--    | 1  | Coke     |
--    | 2  | Juice    |
--    | 3  | Water    |
-- Output :
/*Burger-Coke, Burger-Juice, Burger-Water,
Pizza-Coke, Pizza-Juice, Pizza-Water,
Pasta-Coke, Pasta-Juice, Pasta-Water
*/
-- ===============================================================
-- Create all possible meal combinations (main course + drink)
select 
    main_course, 
    drink 
from MainCourses cross join Drinks

-- Count how many total combinations exist
select 
    count(*) as total_combinations
from MainCourses cross join Drinks

-- List only combinations where main course is "Pizza"
select 
    main_course, 
    drink 
from MainCourses cross join Drinks
where main_course = 'Pizza'


-- ===============================================================
-- Task: Students and Courses Enrollment
/*
    1. Find all students and their courses (include students without courses and courses without enrolled students)
    2. Show students with no courses enrolled
    3. Show courses that have no students enrolled
*/
-- Tables:
/*
Students:
| student_id | student_name |
|------------|--------------|
| 1          | Alice        |
| 2          | Bob          |
| 3          | Carol        |
| 4          | Dave         |

Enrollments:
| student_id | course_name |
|------------|-------------|
| 1          | Math        |
| 1          | Science     |
| 2          | Math        |
| 3          | History     |
| 5          | Biology     |

*/
-- Output: Alice-Math, Alice-Science, Bob-Math, Carol-History, Dave-NULL, NULL-Biology
-- ===============================================================
-- Find all students and their courses (include students without courses and courses without enrolled students)
select 
    student_name,
    course_name
from Students s
full outer join Enrollments e
on s.student_id = e.student_id

-- Show students with no courses enrolled
select 
    student_name,
    course_name
from Students s
full outer join Enrollments e
on s.student_id = e.student_id
where course_name is null

-- Show courses that have no students enrolled
select 
    student_name,
    course_name
from Students s
full outer join Enrollments e
on s.student_id = e.student_id
where student_name is null

-- ===============================================================
-- Task: Employee Hierarchy
/*
    1. Show each employee with their manager's name
    2. Find employees who earn more than their managers
    3. Find all employees who are managers (hint: they appear in manager_id column)
    4. Show the management chain for each employee (employee → manager → top manager)
*/
-- Table:
/*
Employees:
| emp_id | emp_name | manager_id | salary |
|--------|----------|------------|--------|
| 1      | John     | NULL       | 5000   |
| 2      | Mike     | 1          | 4000   |
| 3      | Sarah    | 1          | 4500   |
| 4      | Tom      | 2          | 3500   |
| 5      | Anna     | 2          | 3800   |
| 6      | David    | 3          | 3200   |
*/
-- Output : Mike-John, Sarah-John, Tom-Mike, Anna-Mike, David-Sarah, John-NULL
-- ===============================================================
--Show each employee with their manager's name
select 
    e.emp_name as employee , 
    m.emp_name as manager 
from Employees e
left join Employees m
on e.manager_id = m.emp_id

--Find employees who earn more than their managers
select 
    e.emp_name as employee,
    m.emp_name as manager
from Employees e
left join Employees m
on e.manager_id = m.emp_id
where e.salary > m.salary

--Find all employees who are managers (hint: they appear in manager_id column)
select 
    e.emp_name as employee
from Employees e
inner join Employees m
on e.manager_id = m.emp_id

--Show the management chain for each employee (employee → manager → top manager)
select 
     e.emp_name||'→'|| coalesce(m.emp_name, 'Top manager') as manager
from Employees e
left join Employees m
on e.manager_id = m.emp_id
-- ===============================================================
-- Task:  E-commerce Analysis
/*
    1. Create a "potential market" analysis showing all possible customer-product combinations (Cross Join)
    2. Find all customers and their orders, including customers with no orders and orders with invalid customers (Full Outer Join)
*/
-- Table:
/*
    Products:
    | product_id | product_name | category  |
    |------------|--------------|-----------|
    | 1          | Laptop       | Electronics |
    | 2          | T-Shirt      | Clothing    |
    | 3          | Book         | Education   |
    
    Customers:
    | customer_id | customer_name | city     |
    |-------------|---------------|----------|
    | 1           | Alex          | New York |
    | 2           | Maria         | London   |
    
    Orders:
    | order_id | customer_id | product_id |
    |----------|-------------|------------|
    | 101      | 1           | 1          |
    | 102      | 1           | 2          |
    | 103      | 2           | 1          |
    | 104      | 3           | 4          | -- customer 3 doesn't exist
*/
-- ===============================================================
--Create a "potential market" analysis showing all possible customer-product combinations (Cross Join)
select 
    product_name,
    category,
    customer_name,
    city
from Products cross join Customers

--Find all customers and their orders, including customers with no orders and orders with invalid customers (Full Outer Join)
select 
    c.product_name,
    c.category,
    o.customer_name,
    o.city
from Customers c
full outer join Orders o on c.customer_id = o.customer_id
left join Products p on o.product_id = p.product_id
    
-- ===============================================================
-- Task:  Real-World Problem Solving
-- Problem: A company wants to create a training schedule where each employee must complete each training module.
/*
    1. Generate the complete training schedule (all combinations)
    2. Find which training modules each employee still needs to complete
    3. Identify employees who haven't started any training
*/
-- Tables:
/*
    Employees: [E1, E2, E3]
    Training_Modules: [M1, M2, M3, M4]
    Completed_Training: [(E1, M1), (E1, M2), (E3, M1)]
*/
-- ===============================================================
