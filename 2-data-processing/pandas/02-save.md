## Basic Saving Commands

| File Type | Save Command | What it's for |
| :--- | :--- | :--- |
| **CSV** | `.to_csv()` | Most common format, good for sharing |
| **Excel** | `.to_excel()` | For Excel files with formatting |
| **JSON** | `.to_json()` | For web applications and APIs |

---

## Basic Examples

### 1. Saving to CSV (Most Common)

```python
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
})

# Save to CSV
df.to_csv('employees.csv', index=False)  # index=False avoids saving row numbers
print("✅ Saved to employees.csv")
```

### 2. Saving to Excel

```python
# Save to Excel
df.to_excel('employees.xlsx', index=False)
print("✅ Saved to employees.xlsx")
```

### 3. Saving to JSON

```python
# Save to JSON
df.to_json('employees.json', orient='records', indent=2)
print("✅ Saved to employees.json")
```

---

## Practice Tasks with Previous Data

### Task 1: Save Cleaned Employee Data

```python
# Read your employee data
employee_data = pd.read_csv(r"D:\Data engineering\de-journey\2-data-processing\pandas\employee_data.csv")

# Save it in different formats
employee_data.to_csv(r"D:\Data engineering\de-journey\2-data-processing\pandas\employee_data_clean.csv", index=False)
employee_data.to_excel(r"D:\Data engineering\de-journey\2-data-processing\pandas\employee_data_clean.xlsx", index=False)
employee_data.to_json(r"D:\Data engineering\de-journey\2-data-processing\pandas\employee_data_clean.json", orient='records', indent=2)

print("✅ Saved employee data in 3 formats!")
```

### Task 2: Save Filtered Data

```python
# Read salary data and save only high earners
salary_data = pd.read_csv(r"D:\Data engineering\de-journey\2-data-processing\pandas\Dataset salary 2024.csv")

# Filter for high salaries (adjust the threshold as needed)
high_earners = salary_data[salary_data['Salary'] > 50000]

# Save the filtered data
high_earners.to_csv(r"D:\Data engineering\de-journey\2-data-processing\pandas\high_earners.csv", index=False)
print(f"✅ Saved {len(high_earners)} high earners to file!")
```

### Task 3: Save Processed Data from Multiple Sheets

```python
# Read and combine Excel sheets, then save
df_january = pd.read_excel(r"D:\Data engineering\de-journey\2-data-processing\pandas\sales.xlsx", sheet_name='January')
df_february = pd.read_excel(r"D:\Data engineering\de-journey\2-data-processing\pandas\sales.xlsx", sheet_name='February')

# Combine and save
combined_sales = pd.concat([df_january, df_february], ignore_index=True)
combined_sales.to_csv(r"D:\Data engineering\de-journey\2-data-processing\pandas\combined_sales_2024.csv", index=False)
combined_sales.to_excel(r"D:\Data engineering\de-journey\2-data-processing\pandas\combined_sales_2024.xlsx", index=False)

print("✅ Combined and saved sales data!")
```

---

## ⚙️ Important Parameters

### For CSV Files:
```python
df.to_csv('file.csv', 
          index=False,        # Don't save row numbers
          sep=',',           # Separator (can use ';', '\t')
          header=True,       # Include column names
          encoding='utf-8')  # Character encoding
```

### For Excel Files:
```python
df.to_excel('file.xlsx',
            index=False,        # Don't save row numbers
            sheet_name='Data',  # Sheet name
            engine='openpyxl')  # Excel engine
```

### For JSON Files:
```python
df.to_json('file.json',
           orient='records',  # Format: 'records', 'split', 'index'
           indent=2)          # Pretty printing
```

---

##  Advanced Saving Techniques

### 1. Save Multiple DataFrames to One Excel File

```python
with pd.ExcelWriter('multiple_sheets.xlsx') as writer:
    df_january.to_excel(writer, sheet_name='January', index=False)
    df_february.to_excel(writer, sheet_name='February', index=False)
    high_earners.to_excel(writer, sheet_name='High_Earners', index=False)

print("✅ Saved multiple DataFrames to one Excel file!")
```

### 2. Save with Specific Columns Only

```python
# Save only specific columns
employee_data[['Name', 'Salary']].to_csv('employee_names_salaries.csv', index=False)
print("✅ Saved only Name and Salary columns!")
```

### 3. Save with Custom Formatting (Excel)

```python
# Create Excel file with formatting
with pd.ExcelWriter('formatted_data.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Data', index=False)
    
    # Get the worksheet to apply formatting
    worksheet = writer.sheets['Data']
    
    # Auto-adjust column widths
    for column in worksheet.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2)
        worksheet.column_dimensions[column_letter].width = adjusted_width

print("✅ Saved with formatted Excel file!")
```

---

## Error Handling

```python
try:
    df.to_csv('output.csv', index=False)
    print("✅ File saved successfully!")
except PermissionError:
    print("❌ Error: File might be open in another program!")
except Exception as e:
    print(f"❌ Error saving file: {e}")
```

---

## Quick Reference Card

```python
# Most common save operations:
df.to_csv('data.csv', index=False)                    # Save as CSV
df.to_excel('data.xlsx', index=False)                 # Save as Excel
df.to_json('data.json', orient='records', indent=2)   # Save as JSON

# For multiple sheets in Excel:
with pd.ExcelWriter('data.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)
```

3. Save multiple DataFrames to one Excel file with different sheets

Which saving method would you like to try first? 🚀
