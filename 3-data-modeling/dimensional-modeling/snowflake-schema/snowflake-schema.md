## **Snowflake Schema**

Think of a **snowflake schema as a "normalized" star schema** where dimension tables branch out like snowflake crystals.

---

### **Pizza Restaurant Example:**

**In Star Schema** (for comparison):
```
                     [SALES FACT]
                    /     |     \
                   /      |      \
          [Customer]  [Product]  [Date]
```

**In Snowflake Schema**:
```
                     [SALES FACT]
                    /     |     \
                   /      |      \
          [Customer]  [Product]  [Date]
              ↓           ↓
        [City] ↓     [Category] ↓
          [State]        [Supplier]
```

---

## **❄️ What Makes It Look Like a Snowflake?**

Dimension tables are **split into multiple related tables** (normalized).

### **Example: Product Dimension Snowflaked**

**Instead of one flat Product table:**
| **Product ID** | **Product Name** | **Category** | **Supplier** | **Supplier City** | **Supplier Rating** |
|----------------|------------------|--------------|--------------|-------------------|---------------------|
| P001           | Pepperoni Pizza  | Frozen Foods | ABC Foods    | Chicago           | A+                  |

**Snowflake splits it into:**

**1. PRODUCT TABLE (main dimension)**
| **Product ID** | **Product Name** | **Category ID** | **Supplier ID** |
|----------------|------------------|-----------------|-----------------|
| P001           | Pepperoni Pizza  | CAT-01          | SUP-101         |

**2. CATEGORY TABLE (snowflaked)**
| **Category ID** | **Category Name** | **Department**  |
|-----------------|-------------------|-----------------|
| CAT-01          | Frozen Foods      | Grocery         |
| CAT-02          | Fresh Produce     | Perishables     |

**3. SUPPLIER TABLE (snowflaked)**
| **Supplier ID** | **Supplier Name** | **City ID** | **Rating** |
|-----------------|-------------------|-------------|------------|
| SUP-101         | ABC Foods         | CHI-001     | A+         |

**4. CITY TABLE (snowflaked further!)**
| **City ID** | **City Name** | **State ID** |
|-------------|---------------|--------------|
| CHI-001     | Chicago       | IL-001       |

**5. STATE TABLE**
| **State ID** | **State Name** | **Region** |
|--------------|----------------|------------|
| IL-001       | Illinois       | Midwest    |

See the branching? That's the **snowflake pattern**! ❄️

---

## **🆚 Snowflake vs Star Schema**

**Star Schema (Denormalized):**
```
      [FACT]
    ↙   ↓   ↘
[DIM] [DIM] [DIM]   ← All flat, wide tables
```

**Snowflake Schema (Normalized):**
```
        [FACT]
      ↙   ↓   ↘
    [DIM] [DIM] [DIM]
      ↓     ↙     ↘
    [DIM] [DIM]   [DIM]   ← Branching, normalized tables
```

---

## **✅ Advantages of Snowflake Schema:**

1. **Less Data Redundancy**
   - "Chicago" stored once in City table, not repeated in every supplier record
   - Saves storage space

2. **Easier Maintenance**
   - Update "Illinois" to "IL" in one place (State table)
   - In star schema, you'd update thousands of rows

3. **Better for Complex Hierarchies**
   - Country → State → City → Zip Code chains work naturally

4. **Closer to 3NF (Database Normalization)**
   - Familiar to traditional database designers

---

## **❌ Disadvantages of Snowflake Schema:**

1. **More Complex Queries**
   ```sql
   -- Star Schema (simple):
   SELECT p.category, SUM(s.sales)
   FROM sales_fact s
   JOIN product_dim p ON s.product_id = p.product_id
   
   -- Snowflake (more joins):
   SELECT cat.category_name, SUM(s.sales)
   FROM sales_fact s
   JOIN product p ON s.product_id = p.product_id
   JOIN category cat ON p.category_id = cat.category_id
   ```

2. **Slower Query Performance**
   - More JOINs = Slower queries
   - Star schema is usually faster for analytics

3. **Harder to Understand**
   - More tables to navigate
   - Business users prefer simple star schemas

---

## **🎯 When to Use Snowflake Schema?**

**Good for:**
- **Large dimensions** (millions of customers with addresses)
- **Frequently changing attributes** (prices, categories)
- **When storage is expensive**
- **Traditional RDBMS environments**

**Bad for:**
- **Business intelligence tools** (Tableau, Power BI prefer star)
- **Fast query performance** needs
- **Simple business requirements**
- **Data warehouses** (usually prefer star)

---

## **🏢 Real-World Example: Retail Chain**

**Snowflake Structure:**
```
[Sales Fact]
    ↓
[Store Dim] → [City Dim] → [State Dim] → [Region Dim]
    ↓
[Manager Dim] → [Department Dim]
    ↓
[Product Dim] → [Category Dim] → [Supplier Dim] → [Supplier Country Dim]
```

This allows queries like:
- "Sales by Region" (drill down from Country)
- "Products by Supplier Country"
- "Performance by Manager's Department"

---

## **💡 Pro Tip:**

**Start with Star Schema** (simpler, faster)
**Snowflake only when necessary:**
- Dimension table too large (> millions of rows)
- Significant data redundancy
- Complex hierarchies needed
- Storage constraints

Most modern data warehouses use **hybrid approaches** - star schema with some snowflaking for very large dimensions.

---

## **✅ Quick Summary:**

**Snowflake Schema = Normalized Star Schema**
- **Looks like:** ❄️ (branching crystals)
- **Key idea:** Split dimensions into multiple tables
- **Benefit:** Less redundancy, easier updates
- **Cost:** More complex, slower queries
- **Memory aid:** "Snowflake has many branches, snowflake schema has many tables!"
