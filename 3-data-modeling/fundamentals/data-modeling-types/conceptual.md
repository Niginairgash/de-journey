## E-commerce Conceptual Data Model

**Purpose:** High-level business data representation for stakeholder alignment and system scope definition.

### Simple Explanation - The "Napkin Sketch"

Imagine you're starting an online store. Before worrying about databases or code, you need to answer: **"What are the main things we need to track?"**

Think of it like planning a physical store:
- **Who** comes to your store? → **Customers**
- **What** do you sell? → **Products** 
- **What** happens when someone buys? → **Orders**
- **How** are products organized? → **Categories**
- **Who** gives you products? → **Suppliers**
- **What** do customers think? → **Reviews**

### How These Things Connect (Relationships)

Now, how do these main things interact?
- A **Customer** can place many **Orders**
- An **Order** can contain many **Products**
- A **Product** can belong to many **Categories**  
- A **Supplier** provides many **Products**
- A **Customer** can write many **Reviews**
- A **Product** can receive many **Reviews**


<img width="589" height="341" alt="conceptual diagram e-commerce drawio" src="https://github.com/user-attachments/assets/7358fc18-19d4-467b-b238-a67b64b4c6b8" />



**Key Features:**
- Identifies 6 core business entities
- Defines 6 critical business relationships  
- Uses crow's foot notation for cardinality
- Technology-agnostic business perspective

**Next Steps:** This conceptual model serves as the foundation for logical and physical data modeling phases.
