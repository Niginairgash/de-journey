
## What is a **Hub**? 

**A Hub stores a unique business thing.**

That’s it.

---

## Think like this

A **Hub = a list of unique business identifiers**

Examples of business things:

* Customer
* Order
* Product
* Account

---

## Example: Customer Hub

Imagine we have customers coming from many systems.

### Hub_Customer

| customer_hk | customer_id | load_date  | record_source |
| ----------- | ----------- | ---------- | ------------- |
| HK1         | CUST_001    | 2025-01-01 | CRM           |
| HK2         | CUST_002    | 2025-01-01 | ERP           |

### What is stored here?

* ✅ **Only the business key** (`customer_id`)
* ❌ No name
* ❌ No address
* ❌ No phone

---

## What a Hub **DOES**

* ✔ Stores **unique business key**
* ✔ Combines same entity from many sources
* ✔ Never deletes rows
* ✔ Never updates business keys

---

## What a Hub **DOES NOT**

* ❌ No descriptive attributes
* ❌ No history of changes
* ❌ No relationships

(Those go to **<a href="https://github.com/Niginairgash/de-journey/blob/main/3-data-modeling/data-vault/satellite.md">Satellite</a>** and **<a href="https://github.com/Niginairgash/de-journey/blob/main/3-data-modeling/data-vault/link.md">Link</a>**)

---

## Easy analogy 

**Hub = ID card**

* Name on the card → business key
* Photo, address, age → **not here**

Details go to **<a href="https://github.com/Niginairgash/de-journey/blob/main/3-data-modeling/data-vault/satellite.md">Satellite</a>**

Connections go to **<a href="https://github.com/Niginairgash/de-journey/blob/main/3-data-modeling/data-vault/link.md">Link</a>**

---

## Hub vs Satellite (1 line)

* **Hub** → *Who / What is it?*
* **Satellite** → *What changed over time?*

---

## Typical Hub structure

```sql
hub_customer (
  customer_hk      -- hash key
  customer_id      -- business key
  load_date
  record_source
)
```

---

## One-sentence rule to remember

> **If it uniquely identifies a business entity → it belongs in a Hub**




