-- ===============================================================
-- Author: Nigina Irgasheva
-- Date: 2025-10-14
-- Topic: CTE
-- Task: Create a recursive CTE that generates a sequence of numbers from 1 to 10.
-- ===============================================================
with recursive numbers as(
    select 1 as n
    union all
    select n + 1 from numbers where n < 10
)
select * from numbers

-- ===============================================================
-- Task: Find the entire chain of command for employee 'Charlie' (including himself), showing all managers up to the top.
-- Table: employees - id, name, manager_id 
-- Input: INSERT INTO employees VALUES 
                -- (1, 'Alice', NULL),
                -- (2, 'Bob', 1),
                -- (3, 'Charlie', 2),
                -- (4, 'David', 2),
                -- (5, 'Eve', 1);
-- Output Columns: 
                --id | name    | manager_id | level
                -----|---------|------------|------
                --3  | Charlie | 2          | 1
                --2  | Bob     | 1          | 2  
                --1  | Alice   | NULL       | 3
-- ===============================================================
with recursive rec_employees as (
    select id, name, manager_id, 1 as level  from employees
    where name = 'Charlie'

    union all

    select e.id, e.name, e.manager_id, re.level+1 as level
    from employees e
    inner join rec_employees re on e.id = re.manager_id
)
select * from rec_employees order by level desc

-- ===============================================================
-- Task: Find all subcategories of the 'Electronics' category (including nested ones of any level).
-- Table:  categories - id, name, parent_id 
-- Input: INSERT INTO categories VALUES
            -- (1, 'Electronics', NULL),
            -- (2, 'Computers', 1),
            -- (3, 'Laptops', 2),
            -- (4, 'Tablets', 2),
            -- (5, 'Phones', 1),
            -- (6, 'Smartphones', 5),
            -- (7, 'Accessories', 1);
-- Output Columns: 
            -- id | name         | parent_id
            -- ---|--------------|----------
            -- 1  | Electronics  | NULL
            -- 2  | Computers    | 1
            -- 3  | Laptops      | 2
            -- 4  | Tablets      | 2
            -- 5  | Phones       | 1
            -- 6  | Smartphones  | 5
            -- 7  | Accessories  | 1
-- ===============================================================
with recursive rec_categories as(
    select id, name, parent_id as parent_id from categories
    where name = 'Electronics'

    union all

    select 
        c.id, 
        c.name, 
        c.parent_id
    from categories c 
    inner join rec_categories rc on c.parent_id = rc.id
)
select * from rec_categories

-- ===============================================================
-- Task: For each category, show the full path from the root using the '→' symbol.
-- Input Tables: categories
-- Output Columns: 
            -- id | name        | path
            -- ---|-------------|-----------------------
            -- 1  | Electronics | Electronics
            -- 2  | Computers   | Electronics → Computers
            -- 3  | Laptops     | Electronics → Computers → Laptops
            -- 4  | Tablets     | Electronics → Computers → Tablets
            -- 5  | Phones      | Electronics → Phones
            -- 6  | Smartphones | Electronics → Phones → Smartphones
            -- 7  | Accessories | Electronics → Accessories
-- ===============================================================
with recursive rec_categories as(
    select 
        id, 
        name, 
        parent_id,
        name as path 
    from categories
    where parent_id is NULL

    union all

    select 
        c.id,
        c.name,
        c.parent_id,
        rc.path || '→' || c.name as path
    from categories c
    inner join rec_categories rc on c.parent_id = rc.id
)
select * from rec_categories


-- ===============================================================
-- Task: Find for each manager the number of all his direct and indirect subordinates (including his subordinates' subordinates, etc.).
-- Input Tables: employees
-- Output: 
        -- manager_id | manager_name | subordinates_count
        -- -----------|--------------|-------------------
        -- 1          | Alice        | 4
        -- 2          | Bob          | 2
        -- 3          | Charlie      | 0
        -- 4          | David        | 0
        -- 5          | Eve          | 0
-- ===============================================================

