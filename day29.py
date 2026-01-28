# Day 29 - Pandas Introduction

import pandas as pd

print("="*60)
print("        PANDAS PRACTICE - DAY 29")
print("="*60)

# ============================================
# EXERCISE 1: Create Student Records
# ============================================

print("\n1. STUDENT RECORDS")
print("-"*60)

students = {
    'Name': ['Ahmed', 'Fatima', 'Ibrahim', 'Aisha', 'Yusuf'],
    'Math': [85, 92, 78, 88, 95],
    'English': [78, 85, 92, 80, 88],
    'Science': [90, 88, 85, 92, 90]
}

df = pd.DataFrame(students)

print(df)

# Calculate average for each student
df['Average'] = (df['Math'] + df['English'] + df['Science']) / 3
df['Average'] = df['Average'].round(2)  # Round to 2 decimals

print("\nWith averages:")
print(df)

# ============================================
# EXERCISE 2: Product Inventory
# ============================================

print("\n2. PRODUCT INVENTORY")
print("-"*60)

products = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'],
    'Price': [50000, 30000, 25000, 15000, 5000],
    'Stock': [10, 25, 15, 30, 50]
}

inventory = pd.DataFrame(products)

# Calculate total value
inventory['Total Value'] = inventory['Price'] * inventory['Stock']

print(inventory)

# Total inventory worth
total_worth = inventory['Total Value'].sum()
print(f"\nTotal Inventory Worth: ₦{total_worth:,}")

# ============================================
# EXERCISE 3: Save and Load Data
# ============================================

print("\n3. SAVE TO CSV")
print("-"*60)

# Save student data to CSV
df.to_csv('students.csv', index=False)
print("✅ Saved students.csv")

# Save inventory to CSV
inventory.to_csv('inventory.csv', index=False)
print("✅ Saved inventory.csv")

# Load back
loaded_students = pd.read_csv('students.csv')
print("\nLoaded from CSV:")
print(loaded_students.head())

# ============================================
# EXERCISE 4: Basic Statistics
# ============================================

print("\n4. STATISTICS")
print("-"*60)

print("Student Math scores:")
print(f"Average: {df['Math'].mean():.2f}")
print(f"Highest: {df['Math'].max()}")
print(f"Lowest: {df['Math'].min()}")
print(f"Total students: {len(df)}")

print("\n✅ Day 29 Complete!")
