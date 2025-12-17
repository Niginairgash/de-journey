-- Star Schema: Technical Architecture
-- Core Components

-- 1. Fact Table
-- Grain: One row per business event (e.g., sale, click, shipment)

CREATE TABLE fact_sales (
    -- Surrogate Keys (FKs to dimensions)
    date_key        INT NOT NULL,  -- Degenerate dimension: date
    product_key     INT NOT NULL,
    customer_key    INT NOT NULL,
    store_key       INT NOT NULL,
    -- Degenerate Dimensions (no separate dim table)
    transaction_id  VARCHAR(50),   -- Natural business key
    -- Measures (additive/non-additive/semi-additive)
    sales_amount    DECIMAL(10,2), -- Additive: SUM works
    quantity        INT,           -- Additive
    unit_cost       DECIMAL(10,2), -- Non-additive: AVG needed
    profit_margin   DECIMAL(5,2),  -- Semi-additive: care with time
    -- Metadata
    load_timestamp  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    batch_id        INT
);


--2. Dimension Tables
-- Slowly Changing Dimensions (SCD) Type 2 
create  table core.dim_inventory(
	inventory_pk integer not null,
	inventory_id integer not null,
	film_id integer not null,
	title varchar(255) not null,
	rentel_duration int2 not null,
	rental_rate numeric(4, 2) not null,
	length int2,
	rating varchar(10),
	primary key(inventory_pk)
)



-- Typical star query pattern
SELECT 
    d.year,
    d.quarter,
    p.category,
    s.region,
    SUM(f.sales_amount) AS total_sales,
    COUNT(*) AS transaction_count
FROM fact_sales f
JOIN dim_date d      ON f.date_key = d.date_key
JOIN dim_product p   ON f.product_key = p.product_key
JOIN dim_store s     ON f.store_key = s.store_key
WHERE d.year = 2024
    AND p.category = 'Electronics'
    AND s.region = 'North America'
GROUP BY 
    d.year, d.quarter, 
    p.category, s.region
-- Query optimizer recognizes star pattern and uses:
-- 1. Foreign key constraints for join elimination
-- 2. Bitmap filtering on dimension predicates
-- 3. Star join transformation (in columnar DBs)
