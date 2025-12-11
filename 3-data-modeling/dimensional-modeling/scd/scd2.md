# 🟩 **SCD2**

**SCD2 means: every time a value changes, we create a NEW ROW and keep the old one.
We store FULL HISTORY.**

---

## 📌 Imagine a card with our friend's information:

### **At first:**

| ID | Name  | City     | Start Date | End Date |
| -- | ----  | -------- | ---------- | -------- |
| 1  | Zebo  | Dushanbe | 2024-01-01 | NULL     |

Ali moves to Khujand.

👉 **With SCD2 we DO NOT overwrite the old row.**
We **close** the old version and **create a new one**.

### **After change:**

| ID | Name  | City     | Start Date | End Date   |
| -- | ----  | -------- | ---------- | ---------- |
| 1  | Zebo  | Dushanbe | 2024-01-01 | 2024-05-10 |
| 1  | Zebo  | Khujand  | 2024-05-11 | NULL       |

---

# 🧠 What SCD2 does:

* ✔ Keeps **full history**
* ✔ Stores **old versions**
* ✔ Always creates **new row**
* ✔ Uses **start/end dates**
* ✔ Allows us to know *when a value changed*

---

# 🟥 What SCD2 does NOT do:

* ❌ It does NOT overwrite data
* ❌ It does NOT lose old values
* ❌ It does NOT store only the latest data (that’s SCD1)

---

# 🧀 Simple real-life example

If our bank tracks your **address history**:

* Address in 2021 → one row
* Address in 2023 → new row
* Address in 2025 → new row again

They keep everything — that is **SCD2**.


