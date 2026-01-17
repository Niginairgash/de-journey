##  Data Quality

**Data Quality** is the degree to which data is **accurate, complete, consistent, timely, and fit for use** in analytics and decision-making.

---

###  Core Data Quality Dimensions

1. **Accuracy** – data reflects real-world values
2. **Completeness** – no missing required fields
3. **Consistency** – no conflicts across systems
4. **Timeliness** – data is up to date
5. **Uniqueness** – no duplicates
6. **Validity** – data follows rules and formats

---

###  Data Engineer’s Role

A Data Engineer:

* detects data quality issues
* measures quality
* logs & alerts
* prevents bad data propagation

---

###  Common Data Quality Checks

* NOT NULL constraints
* PK / FK checks
* Range & domain checks
* Duplicate detection
* Freshness checks

---

###  Data Quality by Layer

| Layer      | Focus                |
| ---------- | -------------------- |
| Raw / ODS  | schema, types, nulls |
| Core DWH   | keys, relations      |
| Data Marts | metrics & aggregates |

---

###  Data Vault 2.0

* **Hubs** → business key uniqueness
* **Links** → relationship validity
* **Satellites** → historization & attributes
* Often implemented via **DQ views or tests**

