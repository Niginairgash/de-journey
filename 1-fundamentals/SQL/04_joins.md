**Cross Join (Cartesian Product)**

**What it does:** Combines EVERY row from the first table with EVERY row from the second table.

    -- Example tables
    Students:           Subjects:
    | id | name  |      | id | subject   |
    |----|-------|      |----|-----------|
    | 1  | Alice |      | 1  | Math      |
    | 2  | Bob   |      | 2  | Science   |
    
    -- Cross Join
    SELECT * FROM Students CROSS JOIN Subjects;
    
    -- Result:
    | id | name  | id | subject |
    |----|-------|----|---------|
    | 1  | Alice | 1  | Math    |
    | 1  | Alice | 2  | Science |
    | 2  | Bob   | 1  | Math    |
    | 2  | Bob   | 2  | Science |

**Use case:** When you need all possible combinations (like creating a schedule).


**Full Outer Join**

**What it does:** Shows ALL records from BOTH tables, matching where possible and showing NULLs where no match exists.

    -- Example tables
    Employees:          Departments:
    | id | name  | dept_id |  | id | dept_name  |
    |----|-------|---------|  |----|------------|
    | 1  | Alice | 101     |  | 101| Sales      |
    | 2  | Bob   | 102     |  | 102| Marketing  |
    | 3  | Carol | 999     |  | 103| HR         |
    | 4  | Dave  | NULL    |
    
    -- Full Outer Join
    SELECT e.name, d.dept_name 
    FROM Employees e 
    FULL OUTER JOIN Departments d ON e.dept_id = d.id;
    
    -- Result:
    | name  | dept_name |
    |-------|-----------|
    | Alice | Sales     |
    | Bob   | Marketing |
    | Carol | NULL      |  -- No department with id 999
    | Dave  | NULL      |  -- No department assigned
    | NULL  | HR        |  -- No employees in HR department

**Use case:** When you want to see all records from both tables, including unmatched ones.


**Self Join**

**What it does:** Joins a table with ITSELF (usually to compare rows within the same table).

    -- Example: Employees table with manager relationships
    Employees:
    | id | name  | manager_id |
    |----|-------|------------|
    | 1  | Alice | NULL       |  -- CEO, no manager
    | 2  | Bob   | 1          |  -- Managed by Alice (id 1)
    | 3  | Carol | 1          |  -- Managed by Alice (id 1)
    | 4  | Dave  | 2          |  -- Managed by Bob (id 2)
    
    -- Self Join to show employees with their managers
    SELECT e.name AS employee, m.name AS manager
    FROM Employees e
    LEFT JOIN Employees m ON e.manager_id = m.id;
    
    -- Result:
    | employee | manager |
    |----------|---------|
    | Alice    | NULL    |  -- No manager
    | Bob      | Alice   |
    | Carol    | Alice   |
    | Dave     | Bob     |

**Use case:** Hierarchical data (employees-managers), comparing rows within same table.
