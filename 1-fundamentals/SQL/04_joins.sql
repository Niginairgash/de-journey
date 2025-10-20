-- ===============================================================
-- Author: Nigina Irgasheva
-- Date: 2025-10-20
-- Topic: Cross Join, Full Outer Join , Self Join
-- Task: Restaurant Menu Combinations
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


-- ===============================================================
-- Task: Students and Courses Enrollment
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


-- ===============================================================
-- Task: Employee Hierarchy
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
