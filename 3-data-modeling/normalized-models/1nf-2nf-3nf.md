**Normalization** is the process of organizing data in a database to reduce redundancy and improve data integrity.

## Why Do We Need It? (The Problems It Solves)
Without normalization, a database can suffer from three main types of "anomalies" (problems):

1. **Insertion Anomaly:** You can't add a new record because you're missing some unrelated information.
    * Example: You can't add a new product to the system until at least one customer has ordered it.

2. **Update Anomaly:** You have to update the same piece of information in multiple places.
    * Example: If a customer changes their address, you have to find and update every single order they've ever placed. If you miss one, the data is inconsistent.

3. **Deletion Anomaly:** Deleting one record accidentally deletes other, unrelated information.
    * Example: If you delete a customer's only order, you might also lose all their contact information.

---
### The Problem: A Messy Notebook

Imagine you have a single notebook where you write everything about your friends' orders at a café:

| CustomerName  | Order | Phone       | Food           | Price |
|-------------|-------|-------------|--------------|-------|
| Firuz       | 1     | 123-4567    | Osh, Qurutob, Choy | 45, 20, 2 |
| Parvina     | 2     | 765-4321    | Sambusa      | 5     |
| Firuz       | 3     | 123-4567    | Qurutob      | 20    |

This list is messy and causes problems:
* **Update Problem:** If Firuz gets a new phone number, you must find and change it in two places.
* **Delete Problem:** If you erase Parvina's order, you lose her phone number forever.
* **Insert Problem:** You can't add a new customer named Shahin until he actually places an order.

Normalization fixes this by giving us rules to organize our data.

---

### 1NF: The "One Piece of Information Per Box" Rule

**Rule: Each cell must have only one, single piece of information. No lists.**

Our table breaks this rule because the "Food" and "Price" cells for Firuz's first order have lists (`Osh, Qurutob, Choy` and `45, 20, 2`).

**How we fix it:** We break each item in the list into its own row.

**After 1NF:**

| CustomerName | Order | Phone     | Food     | Price |
|------------|-------|-----------|----------|-------|
| Firuz      | 1     | 123-4567  | Osh      | 45    |
| Firuz      | 1     | 123-4567  | Qurutob  | 20    |
| Firuz      | 1     | 123-4567  | Choy     | 2     |
| Parvina    | 2     | 765-4321  | Sambusa  | 5     |
| Firuz      | 3     | 123-4567  | Qurutob  | 20    |

**Now, every cell has just one value. This is 1NF!**

---

### 2NF: The "Facts Belong to the Whole Key" Rule

**Rule: Every fact (like Phone or Food Price) must be a fact about the *entire* key of the table.**

Our 1NF table has a problem. The key is `(Order, Food)` because that's what uniquely identifies a row.
* **Food Price** depends on the **whole key**? No! The price of `Qurutob` is always 20, no matter which order it's in. It only depends on the `Food`, not the whole `(Order, Food)` key. This is a "partial dependency."

**How we fix it:** We split the table. We put anything that doesn't depend on the whole key into its own table.

**After 2NF:**

**Table 1: Order_Items** (This table's key is the whole `(Order, Food)`)
| Order | Food     |
|-------|----------|
| 1     | Osh      |
| 1     | Qurutob  |
| 1     | Choy     |
| 2     | Sambusa  |
| 3     | Qurutob  |

**Table 2: Food_Menu** (This table's key is just `Food`)
| Food     | Price |
|----------|-------|
| Osh      | 45    |
| Qurutob  | 20    |
| Choy     | 2     |
| Sambusa  | 5     |

**Table 3: Order_Owner** (This table's key is just `Order`)
| Order | CustomerName | Phone     |
|-------|------------|-----------|
| 1     | Firuz      | 123-4567  |
| 2     | Parvina    | 765-4321  |
| 3     | Firuz      | 123-4567  |

**Now, in each table, every piece of information is a fact about the *entire* key. This is 2NF!**

---

### 3NF: The "Facts are Direct" Rule

**Rule: A fact must be a fact about *only* the key, and nothing else.**

Our `Order_Owner` table from 2NF still has a problem. Let's look at it:
| Order | CustomerName | Phone     |
|-------|------------|-----------|

The key is `Order`.
* **CustomerName** depends on the key `Order`? Yes. Order #1 was made by Firuz.
* **Phone** depends on the key `Order`? Not directly. The phone number belongs to **Firuz**, not to the order. If Firuz changes his number, we have to update it in two orders. This is a "transitive dependency."

**How we fix it:** We move the non-key fact (Phone) to its own table, connected to the customer.

**After 3NF:**

**Table A: Orders** (Key is `Order`)
| Order | CustomerID |
|-------|------------|
| 1     | 101        |
| 2     | 102        |
| 3     | 101        |

**Table B: Customers** (Key is `CustomerID`)
| CustomerID | CustomerName | Phone     |
|------------|------------|-----------|
| 101        | Firuz      | 123-4567  |
| 102        | Parvina    | 765-4321  |

**(We still have our `Order_Items` and `Food_Menu` tables from 2NF)**

**Now, in the `Orders` table, every piece of information is a direct fact about the `Order` key. Firuz's phone number is stored only once. This is 3NF!**

### Simple Summary

*   **1NF:** No lists. One value per box.
*   **2NF:** Every fact is a fact about the *whole* key of its table.
*   **3NF:** Every fact is a fact about *only* the key, and no other facts.

By following these rules, we organized our messy list into a clean, efficient database where information is stored only once!
