## LOGGING IN DATA PIPELINES

### What is logging in pipelines

**Logging** is the process of recording technical information about pipeline execution:

* what started
* when and with which parameters
* what succeeded
* where and why failures happened

Logging is essential for **debugging, monitoring, and operating** data pipelines.

---

### Why logging is important

1. **Debugging**
   Identify *where* and *why* a pipeline failed.

2. **Monitoring**
   Track:

   * processed row counts
   * execution time
   * data quality issues

3. **Audit & reproducibility**
   Critical for enterprise DWH:

   * who ran the pipeline
   * what data was loaded
   * which code version was used

4. **Production readiness**
   A pipeline without logs is **not production-ready**.

---

### What to log in a data pipeline

#### 1. Log levels

* **INFO** — normal execution
  `Pipeline started`, `Loaded 1,000,000 rows`
* **WARNING** — non-critical issues
  `Null values detected`, `Late arriving data`
* **ERROR** — step failed, pipeline may continue
  `Failed to parse record`
* **CRITICAL** — pipeline stopped
  `Database connection lost`

---

#### 2. Logging content

For each step:

* pipeline name
* step name (extract / transform / load)
* source and target tables
* row counts (input / output)
* execution time
* status (SUCCESS / FAILED)
* error message (if any)

---

### Logging and architecture

#### Medallion Architecture

* **Bronze** — log ingestion, source issues, raw data quality
* **Silver** — log transformations, cleansing, deduplication
* **Gold** — log business metrics and aggregates

---

#### Data Vault 2.0

* log loads for:

  * hubs (new business keys)
  * links (relationships)
  * satellites (changes, SCD2)
* additionally log:

  * hash keys
  * new vs changed records
  * record source

---

### Where to store logs

* stdout (Docker / Kubernetes)
* log files
* audit tables in DWH (`etl_log`, `load_audit`)
* monitoring tools (Airflow UI, Grafana, ELK)
