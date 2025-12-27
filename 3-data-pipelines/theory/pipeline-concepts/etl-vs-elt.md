### ETL (Extract → Transform → Load)

**What it is:**
Data is **extracted**, **transformed**, and **then loaded** into the data warehouse.

**How it works:**

1. **Extract** data from source systems
2. **Transform** data (cleaning, aggregations, business rules)
3. **Load** processed data into DWH

**Where transformations happen:**
➡️ Outside the data warehouse

**Pros:**

* Clean data before loading
* Strong data quality control
* Suitable for traditional DWH

**Cons:**

* Slower with large volumes
* Limited scalability
* Less flexible

**When to use:**

* On-premise data warehouses
* Limited DB resources
* Strict data governance

---

### ELT (Extract → Load → Transform)

**What it is:**
Data is **extracted**, **loaded first**, and **transformed inside the data warehouse**.

**How it works:**

1. **Extract** data
2. **Load** raw data into DWH
3. **Transform** using SQL in DWH

**Where transformations happen:**
➡️ Inside the data warehouse

**Pros:**

* High performance and scalability
* Uses cloud and MPP power
* Very flexible for analytics
* Ideal for Data Vault 2.0

**Cons:**

* Raw data stored in DWH
* Requires strong modeling discipline

**When to use:**

* Cloud data warehouses
* Big Data environments
* Modern data platforms

---

### 🔹 Quick Comparison

| Criteria       | ETL         | ELT        |
| -------------- | ----------- | ---------- |
| Transformation | Before load | After load |
| Processing     | External    | Inside DWH |
| Scalability    | Low         | High       |
| Cloud-ready    | ❌           | ✅          |
| Data Vault 2.0 | ❌           | ✅          |
