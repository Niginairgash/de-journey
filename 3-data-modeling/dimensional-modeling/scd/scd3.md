# 🟨 **SCD3**

**SCD3 keeps ONLY some history, not full history.
We store the CURRENT value and ONE (or few) PREVIOUS values in the same row.
No new rows.**

---

## 📌 Example

### At first:

| ID | Name  | City (Current) | City (Previous) |
| -- | ----  | -------------- | --------------- |
| 1  | Zebo  | Dushanbe       | NULL            |

Zebo moves to Khujand.

👉 **With SCD3 we DO NOT create a new row.**
👉 **We shift the values inside the SAME row.**

### After change:

| ID | Name  | City (Current) | City (Previous) |
| -- | ----  | -------------- | --------------- |
| 1  | Zebo  | Khujand        | Dushanbe        |

If Zebo moves again to Bokhtar:

### After second change:

| ID | Name | City (Current) | City (Previous) |
| -- | ---- | -------------- | --------------- |
| 1  | Ali  | Bokhtar        | Khujand         |

Oldest history is lost.
You only keep **limited history (1 step back)**.

---

# 🧠 What SCD3 does:

✔ Stores current value
✔ Stores previous value(s)
✔ Keeps **limited** history
✔ No new rows (same record)
✔ Easy to query

---

# 🟥 What SCD3 does NOT do:

❌ No full history
❌ Does not track every change
❌ Loses older values after each update
❌ No start/end date range like SCD2

---

# 🎯 When is SCD3 used?

* When you need **only the last known value**, not full history
* When business wants to compare “current vs previous”
* When table must remain small and simple

Examples:

* Customer current and previous subscription plan
* Employee current and previous job title
