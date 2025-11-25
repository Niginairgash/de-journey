##  Logical Data Modeling - The "Blueprint"

### Simple Explanation - The Detailed Blueprint

Now that we have our "napkin sketch" (conceptual model), it's time to create the **detailed blueprint**. Think of this as the architect's detailed plans:

- We're still **not** choosing specific database technology
- We're **adding details** to each entity
- We're figuring out **exactly how things connect**
- We're applying **organization rules** (<a href="https://github.com/Niginairgash/de-journey/tree/main/3-data-modeling/normalized-models" >normalization</a>)

### What Changes from Conceptual to Logical?

| Conceptual | Logical |
|------------|---------|
| "Customer" | `Customer` table with `CustomerID`, `FirstName`, `LastName`, `Email` |
| "places" relationship | `Order` table with `CustomerID` foreign key |
| "Product belongs to Category" | Junction table `Product_Category` |

### Step 1: Define Attributes for Each Entity

Let's add detailed attributes to each of our entities:

#### **Customer Table**
- `CustomerID` (Primary Key)
- `FirstName` 
- `LastName`
- `Email`
- `Phone`
- `RegistrationDate`

#### **Product Table**
- `ProductID` (Primary Key)
- `ProductName`
- `Description`
- `Price`
- `StockQuantity`
- `SupplierID` (Foreign Key)

#### **Order Table**
- `OrderID` (Primary Key)
- `OrderDate`
- `TotalAmount`
- `Status`
- `CustomerID` (Foreign Key)

#### **Category Table**
- `CategoryID` (Primary Key)
- `CategoryName`
- `Description`

#### **Supplier Table**
- `SupplierID` (Primary Key)
- `SupplierName`
- `ContactEmail`
- `Phone`

#### **Review Table**
- `ReviewID` (Primary Key)
- `Rating` (1-5 stars)
- `Comment`
- `ReviewDate`
- `CustomerID` (Foreign Key)
- `ProductID` (Foreign Key)

### Step 2: Handle Many-to-Many Relationships

#### **Order_Product** (for Order contains Product)
- `OrderID` (Foreign Key, part of composite PK)
- `ProductID` (Foreign Key, part of composite PK)
- `Quantity`
- `UnitPrice`

#### **Product_Category** (for Product belongs to Category)
- `ProductID` (Foreign Key, part of composite PK)
- `CategoryID` (Foreign Key, part of composite PK)

### Step 3: Let's Create the Logical Diagram in draw.io

Here's how to transform your conceptual diagram:

#### **New Tables to Add:**
```
[Order_Product]    [Product_Category]
```

#### **Updated Relationships:**
- **Order** → **Order_Product** (1-to-Many)
- **Product** → **Order_Product** (1-to-Many)
- **Product** → **Product_Category** (1-to-Many)
- **Category** → **Product_Category** (1-to-Many)

### Step 4: Complete Logical Model Structure

```
[Customer]────(1)───< (0..*) >───[Order]
  | 1                            | 1
  | |                            | |
  | └──< (0..*) >──[Review]──> (0..*) 
  | 1                  |          1
  |                    |          |
[Supplier]─< (1..*) >─[Product]─< (0..*) >──[Category]
                       |    |               |
                       |    └───[Product_Category]──┘
                       |
                       └───[Order_Product]──┘
```

### Step 5: Key Changes from Conceptual Model

1. **Added primary keys** to all entities
2. **Added foreign keys** for relationships
3. **Created junction tables** for M:N relationships
4. **Defined all attributes** with data types
5. **Applied normalization** (no redundant data)

## E-commerce Logical Data Model

**Transformation from Conceptual:**
- Added detailed attributes with data types
- Implemented junction tables for M:N relationships
- Defined primary and foreign keys
- Applied first normal form (1NF)

**Key Technical Decisions:**
- Used junction tables for Order-Product and Product-Category relationships
- Implemented proper referential integrity through foreign keys
- Added quantity tracking in Order_Product junction table

**Tools:** draw.io with logical modeling notation

### 🎯 Ready for the Next Step?

Our logical model now includes:
- ✅ All detailed attributes
- ✅ Proper relationship implementation
- ✅ Primary and foreign keys
- ✅ Junction tables for M:N relationships

**Next, we'll move to Physical Data Model** where we choose specific database technology (MySQL, PostgreSQL, etc.) and add performance optimizations!

Would you like me to show you how to create this logical diagram in draw.io, or shall we proceed directly to the physical model?
