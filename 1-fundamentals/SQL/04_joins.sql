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
