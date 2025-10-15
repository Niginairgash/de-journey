-- ===============================================================
-- Author: Nigina Irgasheva
-- Date: 2025-10-15
-- Topic: CTE RECURSIVE
-- ===============================================================

-- ===============================================================
-- Task 1. Movie Categories Hierarchy
-- ===============================================================

--Create a fake hierarchy of movie categories.
create temp table category_hierarchy as
select * from
(values
	(1, 'Movies', NULL),
    (2, 'Action', 1),
    (3, 'Comedy', 1),
    (4, 'Romantic Comedy', 3),
    (5, 'Drama', 1),
    (6, 'Crime Drama', 5)
) as t(category_id, category_name, parent_id);

with recursive rec_category_hierarchy as(
    select -- anchor level
        category_id, 
        category_name, 
        parent_id, 
        1 as level, 
        category_name as path 
    from category_hierarchy
	where parent_id is null

    union all

    select  -- recursive level
        ch.category_id, 
        ch.category_name, 
        ch.parent_id,
        level + 1 as level,
        rch.path || '→' || ch.category_name as path
    from category_hierarchy ch
    inner join rec_category_hierarchy rch on ch.parent_id = rch.category_id
)
select * from rec_category_hierarchy order by path;

-- ===============================================================
-- Task 2. Count Movies by Category
-- ===============================================================
with recursive rec_category_hierarchy as(
    select -- anchor level
        category_id, 
        category_name, 
        parent_id, 
        1 as level,
        category_name as path 
    from category_hierarchy
	where parent_id is null

    union all

    select  -- recursive level
        ch.category_id, 
        ch.category_name, 
        ch.parent_id,
        level + 1 as level,
        rch.path || '→' || ch.category_name as path
    from category_hierarchy ch
    left join rec_category_hierarchy rch on ch.parent_id = rch.category_id
)
select 
	rch.category_name,
	rch.level,
	count(fc.category_id) as film_count,
	rch.path
from rec_category_hierarchy rch
left join film_category fc on fc.category_id = rch.category_id
group by 1,2,4
order by path;


