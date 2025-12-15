## When to create Link Satellite

 **Create a Link Satellite when the relationship itself has data or changes over time.**

---

## First, remember roles

* **Link** → *connects Hubs*
* **Link Satellite** → *describes the relationship*

---

## Ask yourself ONE question 

> **Does the relationship have attributes?**

If **YES** → create **Link Satellite**
If **NO** → Link alone is enough

---

## Example 1: Customer places Order ❌ (no Link Satellite)

Relationship:

> Customer ↔ Order

Link:

```text
link_customer_order
```

Does the relationship have attributes?

* Customer has attributes → Satellite on Hub
* Order has attributes → Satellite on Hub

➡ **NO Link Satellite needed**

---

## Example 2: Order contains Product ✅ (Link Satellite needed)

Relationship:

> Order ↔ Product

But the relationship has data:

* quantity
* price_at_order_time
* discount

➡ **These describe the relationship itself**

### Structure:

```text
hub_order
hub_product
link_order_product
sat_link_order_product
```

---

## Example 3: Employee assigned to Project ✅

Relationship data:

* role
* assignment_start_date
* assignment_end_date
* allocation_percent

➡ **Create Link Satellite**

---

## Example 4: Bank Account owned by Customer ❌ / ✅

Case A (simple ownership):

* Customer ↔ Account
* No extra data

➡ No Link Satellite

Case B (ownership has rules):

* ownership_type (primary / secondary)
* valid_from / valid_to

➡ **Link Satellite needed**

---

## What goes into Link Satellite?

* ✔ Attributes of the relationship
* ✔ Historical changes (SCD2 style)
* ✔ Time-dependent data

* ❌ Business keys
* ❌ Foreign keys to other Hubs

---

## Link Satellite example table

```sql
sat_link_order_product (
  link_hk
  quantity
  price
  discount
  load_date
  end_date
  record_source
)
```

---

## Very common mistake 

* ❌ Putting measures into Link
* ❌ Putting relationship attributes into Hub Satellite

➡ Always ask:

> *Is this about the thing or about the connection?*

---

## Data Vault → Star Schema (important)

| Data Vault            | Star Schema |
| --------------------- | ----------- |
| Link + Link Satellite | Fact table  |
| Hub Satellite         | Dimension   |

This is why **Link Satellites are critical** for analytics.

---

## Final rule to remember 

> **If analytics care about the relationship → you need a Link Satellite**


