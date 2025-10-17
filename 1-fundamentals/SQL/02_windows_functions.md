**Basic Window Function Syntax**

    function_name() OVER (
        [PARTITION BY column1, column2...]
        [ORDER BY column1 [ASC|DESC]]
        [window_frame_clause]
    )

**Common Window Functions**

**Ranking Functions**
    
    -- ROW_NUMBER() - Number rows
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC)
    
    -- RANK() - Position in group (may have gaps)
    RANK() OVER (PARTITION BY department ORDER BY sales DESC)
    
    -- DENSE_RANK() - Position in group (no gaps in ranking)
    DENSE_RANK() OVER (PARTITION BY department ORDER BY sales DESC)

**Aggregate Window Functions**

    -- Running total
    SUM(sales) OVER (PARTITION BY region ORDER BY date)
    
    -- Average 
    AVG(revenue) OVER (
        PARTITION BY product 
        ORDER BY month 
    )
    
    -- Count per partition
    COUNT(*) OVER (PARTITION BY department)
    
    -- Min/Max per group
    MIN(salary) OVER (PARTITION BY job_title)
    MAX(sales) OVER (PARTITION BY salesperson)

**Offset Functions**

    -- Previous row's value
    LAG(sales) OVER (PARTITION BY product ORDER BY month)
    
    -- Next row's value  
    LEAD(sales) OVER (PARTITION BY product ORDER BY month)
    
    -- First value in partition
    FIRST_VALUE(price) OVER (PARTITION BY category ORDER BY date)
    
    -- Last value in partition
    LAST_VALUE(price) OVER (PARTITION BY category ORDER BY date)
