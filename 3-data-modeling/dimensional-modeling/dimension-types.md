
## **Dimension Table**

Think of a **dimension table as the "who, what, where, when" guidebook** that gives meaning to the numbers in your fact table.

---

### **Continuing Our Pizza Restaurant Example:**

In our fact table, we see: `Customer ID = C005`, `Pizza Type ID = PZ-101`, `Date = Jan 15, 2023`

But what do these codes mean? That's where dimension tables come in!

---

### **Our Dimension Tables:**

**1. CUSTOMER DIMENSION (Who ordered?)**
| **Customer ID** | **Name**   | **City**    | **Membership** | **Join Date**  |
|-----------------|------------|-------------|----------------|----------------|
| C005            | John Smith | New York    | Gold           | Jan 10, 2022   |
| C010            | Maria Lee  | Boston      | Silver         | Mar 05, 2022   |

**2. PIZZA DIMENSION (What was ordered?)**
| **Pizza Type ID** | **Pizza Name**  | **Category** | **Size** | **Vegetarian?** |
|-------------------|-----------------|--------------|----------|-----------------|
| PZ-101            | Margherita      | Classic      | Large    | Yes             |
| PZ-103            | Pepperoni Feast | Special      | Medium   | No              |

**3. DATE DIMENSION (When was it ordered?)**
| **Date**       | **Day**  | **Month** | **Year** | **Quarter** | **Holiday?** | **Weekend?** |
|----------------|----------|-----------|----------|-------------|--------------|--------------|
| Jan 15, 2023   | Sunday   | January   | 2023     | Q1          | No           | Yes          |

---

### **What Dimension Tables Do:**

They **translate codes into meaningful information** so we can ask questions like:
- "Which **city** (from Customer Dim) ordered the most **vegetarian pizzas** (from Pizza Dim) on **weekends** (from Date Dim)?"

Without dimension tables, we will just see: `C005, PZ-101, 2023-01-15` → Meaningless codes!

---

### **Key Features of Dimension Tables:**

1. **Holds Descriptive Text**
   - Names, categories, descriptions, locations, dates
   - Things we **read** and **filter by**

2. **Answers "Who? What? Where? When?" questions**
   - "Who are my top customers?" → Look in Customer Dimension
   - "What products are in the 'Classic' category?" → Look in Product Dimension

3. **Usually Smaller & Stable**
   - 100 customers, 50 products, 365 days in a year
   - Changes less often than fact tables

4. **Contains Hierarchies** (drill-down paths)
   ```
   Date: Year → Quarter → Month → Day
   Location: Country → State → City → Store
   Product: Category → Subcategory → Product → SKU
   ```

---

### **How They Connect to Fact Table:**

```
FACT TABLE (Sales)
Order ID | Date ID | Customer ID | Pizza ID | Quantity | Price
---------|---------|-------------|----------|----------|-------
1001     | 20230115| C005        | PZ-101   | 2        | $24
         ↓           ↓             ↓
         ↓           ↓             Customer Dimension
         ↓           ↓             Name: John Smith
         ↓           ↓             City: New York
         ↓
         Date Dimension
         Day: Sunday
         Month: January
         Holiday: No
```

---

### **Real-World Dimension Examples:**

**E-commerce:**
- **Product Dim**: Name, category, brand, color, size
- **Customer Dim**: Age group, gender, location, loyalty tier
- **Store Dim**: Store name, region, manager, size (sq ft)
- **Time Dim**: Hour, day part (morning/evening), season

**Hospital:**
- **Doctor Dim**: Specialty, department, years of experience
- **Patient Dim**: Age group, insurance type, admission type
- **Treatment Dim**: Procedure name, category, complexity

**School:**
- **Student Dim**: Grade level, program, extracurriculars
- **Teacher Dim**: Subject, qualification, years teaching
- **Course Dim**: Department, difficulty level, credits

---

### **Special Dimension Types:**

1. **Slowly Changing Dimensions (SCD)**
   - When a customer changes address → How do we update?
   - Type 1: Overwrite old data (simple)
   - Type 2: Keep history (add new row with effective dates)
   - Type 3: Keep limited history (current + previous columns)

2. **Junk Dimensions**
   - Combine small yes/no flags (e.g., `is_holiday`, `is_weekend`, `is_sale_day`)

3. **Degenerate Dimensions**
   - Transaction IDs that don't have their own table (like `Order ID`)

---

### **✅ Quick Summary:**
- **Fact Table** = **Numbers** we calculate (How many? How much?)
- **Dimension Table** = **Text** we describe with (Who? What? Where? When?)
- **Together** = A complete story!

**Simple Test:**
- Can you **SUM** or **AVERAGE** it? → **Fact table column**
- Can you **GROUP BY** or **FILTER** by it? → **Dimension table column**

**Remember:** Dimensions give **context** to facts. Without dimensions, facts are just meaningless numbers!
