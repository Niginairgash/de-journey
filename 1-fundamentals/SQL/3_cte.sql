-- ===============================================================
-- Author: Nigina Irgasheva
-- Date: 2025-10-14
-- Topic: CTE
-- Task: Создайте рекурсивный CTE, который генерирует последовательность чисел от 1 до 10.
-- ===============================================================
with recursive numbers as(
    select 1 as n
    union all
    select n + 1 from numbers where n < 10
)
select * from numbers

-- ===============================================================
-- Task: Найти всю цепочку подчинения для сотрудника 'Charlie' (включая его самого), показав всех менеджеров до самого верха.
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
-- Task: Найти все подкатегории категории 'Electronics' (включая вложенные любого уровня).
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
    c.id, c.name, c.parent_id
    from categories c 
    inner join rec_categories rc on c.parent_id = rc.id
)
select * from rec_categories

-- ===============================================================
-- Task: Для каждой категории показать полный путь от корня через символ '→'.
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
-- Task: Найти для каждого менеджера количество всех его прямых и косвенных подчиненных (включая подчиненных его подчиненных и т.д.).
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

