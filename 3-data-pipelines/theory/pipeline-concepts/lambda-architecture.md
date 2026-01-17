## Lambda Architecture

**Lambda Architecture** is a data processing architecture that combines
**batch processing (accurate but slow)** and **stream processing (fast but approximate)**.

### Why use it?

To achieve:

* **near real-time results**
* **accurate, re-computable data**

---

### Main layers

#### 1. Batch Layer

* Processes **all historical data**
* Slow but **very accurate**
* Can recompute everything from scratch
* Examples: Spark, Hive, Greenplum

---

#### 2. Speed Layer (Streaming Layer)

* Processes **new incoming data immediately**
* Fast but may be **less accurate**
* Works until batch recomputation finishes
* Examples: Kafka Streams, Flink, Spark Streaming

---

#### 3. Serving Layer

* Combines **Batch + Speed results**
* Serves data to BI tools, APIs, dashboards
* Examples: DWH, OLAP stores, ClickHouse

---

### How it works

1. Data arrives as events
2. Speed layer processes data in real time
3. Batch layer periodically recomputes everything
4. Serving layer merges the results

---

### Pros & Cons

**Pros**

* Accurate data
* Real-time analytics
* Fault tolerance

**Cons**

* ❌ Complex architecture
* ❌ Duplicate logic
* ❌ High maintenance cost

---

### Related architectures

* **Kappa Architecture** → only streaming
* **Medallion Architecture** → layered DWH
* **Lambda + Data Vault** → possible but complex
* объяснить, **нужно ли это современному Data Engineer (Senior level)**

