
## 🟦 **SCD1 (Slowly Changing Dimension Type 1)**

**SCD1 means: just replace the old value with the new value.
No history. No past versions. Only the latest state.**

---

### 📌 **Imagine a card with our friend's information:**

| Name  | City     |
| ----- | -------- |
| Zebo  | Dushanbe |

If Zebo moves to Khujand, with **SCD1** you do this:

👉 You overwrite the old city.

| Name  | City    |
| ----  | ------- |
| Zebo  | Khujand |

We **don’t store that he lived in Dushanbe before**.

---

## 🟢 When do we use SCD1?

* When old values are **not important**
* When we **don’t need history**
* Example:

  * Customer’s email
  * Correcting wrong data
  * Fixing typos
  * Non-critical attributes

---

## 🔴 SCD1 does NOT do:

* ❌ No historical tracking
* ❌ No “old version”
* ❌ No dates (start/end)
* ❌ No version numbers

---

## 🧠 Easy example in real life

If our phone number changes, our bank updates the number.
They don’t store all past numbers — they **just keep the latest**.

That’s SCD1.
