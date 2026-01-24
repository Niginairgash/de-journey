# Error handling

## What is error handling

**Error handling** is a set of practices that allow data pipelines to:

* detect errors,
* handle them properly,
* avoid breaking the entire system.

In data engineering, errors are **expected**, not exceptional.

---

## Where errors come from

### 1. Data sources

* API is unavailable
* file not delivered
* schema changes (new / removed columns)

### 2. Data issues

* unexpected `NULL`s
* duplicates
* wrong data types
* business rule violations

### 3. Infrastructure

* container crashes
* disk space issues
* network problems
* timeouts

---

## Core error handling principles

### 1. Fail fast

If data quality is **critical**, the pipeline must fail immediately.
Bad data is worse than no data.

Examples:

* missing business key → **fail**
* empty file → **fail**

---

### 2. Retry

Use retries only for **temporary issues**:

* network
* API
* database availability

Do NOT retry:

* data errors
* logical errors

---

### 3. Logging

Every error must be:

* logged
* understandable
* traceable

Good logs answer:

* what failed
* where
* with which parameters

---

### 4. Error classification

* **Data errors**
* **System errors**
* **Code errors**

Each type requires a different response.

---

### 5. Idempotency

Re-running a pipeline:

* does not duplicate data
* does not corrupt history

This is critical for:

* Airflow
* Data Vault
* incremental loads

---

## Error handling in Airflow

* `retries`
* `retry_delay`
* `on_failure_callback`
* alerts (Email / Telegram)

A failed task:

* does not corrupt previous data
* can be safely re-run

---

## Error handling in ETL / ELT

Typical approach:

* Stage layer → basic checks
* Core layer → strict validation
* Error → stop pipeline
* Success → move forward

https://medium.com/data-engineering-technical-standards-and-best/error-handling-retry-logic-n-data-engineering-5e1922be8b01
