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
-- Slowly Changing Dimensions (SCD) Type 2 Example
CREATE TABLE dim_customer (
    -- Surrogate Key (artificial, stable)
    customer_key     INT PRIMARY KEY IDENTITY(1,1),
    -- Natural/Business Key (from source system)
    customer_id      VARCHAR(20) NOT NULL,
    -- Attributes (descriptive data)
    customer_name    VARCHAR(100),
    customer_segment VARCHAR(50),
    city             VARCHAR(50),
    region           VARCHAR(50),
    -- SCD Type 2 columns
    start_date       DATE NOT NULL,
    end_date         DATE DEFAULT '9999-12-31',
    is_current       BIT DEFAULT 1,
    version_number   INT DEFAULT 1,
    -- Audit columns
    created_date     TIMESTAMP,
    updated_date     TIMESTAMP,
    -- Indexes (for performance)
    INDEX idx_natural_key (customer_id, start_date),
    INDEX idx_current (is_current)
);


-- Technical Characteristics

-- 1. Primary Key Structure

-- Fact Table PK: Composite of all dimension FKs
--               (date_key, product_key, customer_key, store_key)
               
--Dimension PK:  Single surrogate key (customer_key)


-- 2. Referential Integrity**

-- All fact table FKs must point to valid dimension records
ALTER TABLE fact_sales ADD CONSTRAINT fk_product
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key);

-- Snowflake vs Star (avoid this in pure star schema):
-- Star:   fact → dim_product (category included in dim_product)
-- Snowflake: fact → dim_product → dim_category (normalized)


-- 3. Indexing Strategy**

-- Fact Table Indexes:
CREATE CLUSTERED INDEX idx_fact_sales_date 
    ON fact_sales(date_key);  -- Most queries filter by date

CREATE NONCLUSTERED INDEX idx_fact_sales_product 
    ON fact_sales(product_key) INCLUDE (sales_amount, quantity);

-- Dimension Table Indexes:
CREATE INDEX idx_dim_customer_natural 
    ON dim_customer(customer_id, start_date, end_date);

-- Query Performance Patterns

-- Star Join Optimization:

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
