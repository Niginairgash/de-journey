## What is a **Satellite**? 

**A Satellite stores details and history.**

---

## One-line definition 

> **If something can change over time → it belongs in a Satellite**

---

## Satellite answers this question

**“What do we know about this thing, and how did it change?”**

---

## Example: Customer Satellite

### Hub (who?)

```text
hub_customer
customer_id = CUST_001
```

### Satellite (details + history)

| customer_hk | name | address | status | load_date  | end_date   |
| ----------- | ---- | ------- | ------ | ---------- | ---------- |
| HK1         | Anna | NY      | ACTIVE | 2024-01-01 | 2024-06-01 |
| HK1         | Anna | LA      | ACTIVE | 2024-06-01 | NULL       |

➡ Address changed → **new row**, not update

---

## What a Satellite **DOES**

✔ Stores descriptive attributes

✔ Stores historical changes (<a href="https://github.com/Niginairgash/de-journey/blob/main/3-data-modeling/dimensional-modeling/scd/scd2.md">SCD2</a> style)

✔ Can be attached to **Hub or Link**

✔ Can have multiple Satellites per Hub/Link

---

## What a Satellite **DOES NOT**

❌ Business keys

❌ Relationships

❌ Surrogate meaning

---

## Types of Satellites (important)

### 1. Hub Satellite

Describes **one business entity**

Examples:

* Customer name, email, address
* Product name, category, price

---

### 2. Link Satellite

Describes **a relationship**

Examples:

* Order–Product → quantity, price
* Employee–Project → role, dates

---

### 3. Reference Satellite (optional)

Slow-changing lookup data

Examples:

* Country codes
* Currency codes

---

## Easy analogy 

* **Hub** = Person
* **Satellite** = Passport history
* **Link** = Marriage
* **Link Satellite** = Marriage details (date, status)

---

## Typical Satellite structure

```sql
sat_customer_details (
  customer_hk
  name
  address
  status
  load_date
  end_date
  record_source
)
```

---

## Satellite rules to remember 

1. Satellites are **insert-only**
2. Changes = **new row**
3. One Hub → many Satellites allowed
4. Satellites are the **only place for attributes**

---

## Satellite vs Dimension (important for you)

| Data Vault           | Star Schema          |
| -------------------- | -------------------- |
| Satellite            | Dimension attributes |
| History in Satellite | SCD2 Dimension       |
