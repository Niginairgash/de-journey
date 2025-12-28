##  Testing in Data Pipelines 

### What is pipeline testing?

Testing in data pipelines ensures that **data, transformations, and orchestration work correctly** and that changes do not break data quality or business logic.

---

### Types of testing

#### 1. Unit Tests

Test individual components and transformations.

Examples:

* SQL transformations return correct results
* Python functions clean or enrich data correctly
* Stable hash keys (Data Vault)

Tools:

* pytest
* dbt singular tests

---

#### 2. Integration Tests

Verify interactions between pipeline components.

Examples:

* ODS → Data Vault → Data Mart
* Loading data into Greenplum
* Airflow DAG task dependencies

---

#### 3. Data Quality Tests

Validate the **data itself**, not the code.

Common checks:

* NOT NULL
* UNIQUE
* Referential integrity
* Value ranges
* Freshness
* Duplicate detection

Tools:

* dbt tests
* Great Expectations
* Custom SQL checks

---

#### 4. End-to-End (E2E) Tests

Test the full pipeline execution.

Examples:

* DAG runs successfully
* Final tables are populated
* Metrics match expected results

---

### What a Data Engineer should test

* SQL transformations
* Data Vault hubs, links, satellites
* SCD Type 2 logic
* Idempotency
* Late-arriving data
* Schema changes
* Backfills

---

### Minimum testing standard 

* Unit tests for Python code
* SQL / dbt data quality tests
* NULL, duplicate, FK checks
* CI-based test execution
* Clear test documentation
