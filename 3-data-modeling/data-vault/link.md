
## What is a **Link**? (Very simple)

**A Link connects business things together.**

---

## Think like this

* **Hub** = a thing
* **Link** = a relationship between things

---

## Example: Order and Customer

Business fact:

> A **Customer places an Order**

### Hubs

* Hub_Customer
* Hub_Order

### Link

* **Link_Customer_Order**

---

## Link table example

| link_hk | customer_hk | order_hk  | load_date  | record_source |
| ------- | ----------- | --------- | ---------- | ------------- |
| L1      | HK_CUST_01  | HK_ORD_10 | 2025-01-01 | ERP           |

### What is stored here?

* ✅ Only **keys of Hubs**
* ❌ No amounts
* ❌ No names
* ❌ No dates like order_date

---

## What a Link **DOES**

* ✔ Connects Hubs
* ✔ Represents business relationships
* ✔ Can connect **2 or more Hubs**
* ✔ Never updates, never deletes

---

## What a Link **DOES NOT**

* ❌ No descriptive attributes
* ❌ No history
* ❌ No measures

(Those go to **<a href="https://github.com/Niginairgash/de-journey/blob/main/3-data-modeling/data-vault/link_satellite.md">Link Satellite</a>**)

---

## Real-life analogy

* Customer
*  Order

**Link = handshake**

The handshake itself has no details —
details like *when*, *how much*, *status* go to **Satellite**

---

## Many-to-many? Yes ✅

Example:

* Order ↔ Product
  One order → many products
  One product → many orders

➡ **Link_Order_Product**

---

## Typical Link structure

```sql
link_customer_order (
  link_hk
  customer_hk
  order_hk
  load_date
  record_source
)
```

---

## Link + Satellite example

### Link table

| link_hk | customer_hk | order_hk |
| ------- | ----------- | -------- |

### Link Satellite

| link_hk | order_date | total_amount | load_date |

---

## Hub vs Link (1 sentence)

* **Hub** → *What is it?*
* **Link** → *How are things connected?*

---

## Golden rule 

> **If something connects two or more business keys → it belongs in a Link**
