A subquery in SQL is a query nested inside another SQL query. It allows complex filtering, aggregation and data manipulation by using the result of one query inside another. They are an essential tool when we need to perform operations like:

* **Filtering:** selecting rows based on conditions from another query.
* **Aggregating:** applying functions like SUM, COUNT, AVG with dynamic conditions.
* **Updating:** modifying data using values from other tables.
* **Deleting:** removing rows based on criteria from another query.

**Common SQL Clauses for Subqueries**

Clauses that can be used with subqueries are:
* **WHERE:** filter rows based on subquery results.
* **FROM:** treat subquery as a temporary (derived) table.
* **HAVING:** filter aggregated results after grouping.


**Types of Subqueries**

**1. Single-Row Subquery.** Subquery that returns a SINGLE value (like the average)
  * Returns exactly one row as the result.
  * Commonly used with comparison operators such as =, >, <

Let's use a simple _employees_ table:

      |employee_id   |	 name   | salary  | department_id |
      ___________________________________________________
      | 1            |	Alice	| 50000	  |  1            |
      | 2	         |  Bob	    | 75000	  |  1            |
      | 3	         | Charlie  | 82000   |  2            |
      | 4	         | Diana	| 45000	  |  2            |



Example:
    
        SELECT name, salary
        FROM employees
        WHERE salary > (
            SELECT AVG(salary)  -- This inner query runs FIRST
            FROM employees      -- It calculates the average (e.g., 6500)
        );
How it works:

* The database runs the part inside the parentheses first: SELECT AVG(salary) FROM employees. It gets the number 6500.
* Now the main query becomes: SELECT name, salary FROM employees WHERE salary > 6500.
* It then returns Bob and Charlie.

**2. Multi-Row Subquery.** Subquery that returns a LIST of values
*  Returns multiple rows as the result.
*  Requires operators that can handle multiple values, such as IN, ANY or ALL

Let's add a departments table:

      | department_id  |department_name
      ________________________________
      |    1	       |   IT
      |    2	       |   Sales
      |    3	       |   HR

   
  Example:
   
       SELECT name
       FROM employees
       WHERE department_id IN (
            SELECT department_id          -- This inner query runs FIRST
            FROM departments              -- It finds the IDs for IT and Sales (1 and 2)
            WHERE department_name IN ('IT', 'Sales')
       );

   **How it works:**
  1. The database runs the inner query: SELECT department_id FROM departments WHERE department_name IN ('IT', 'Sales'). It gets the list (1, 2).
  2. The main query becomes: SELECT name FROM employees WHERE department_id IN (1, 2).
  3. It returns all four employees (Alice, Bob, Charlie, Diana).


**3. Correlated Subquery**
* A dependent subquery: it references columns from the outer query.
* Executed once for each row of the outer query, making it slower for large datasets.

Example:

      SELECT e.Name, e.Salary
      FROM Employees e
      WHERE e.Salary > (SELECT AVG(Salary) 
                  FROM Employees 
                  WHERE DepartmentID = e.DepartmentID);

**Output:** Returns employees earning more than the average salary of their own department.
