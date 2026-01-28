# Day 31 - Complete Data Manipulation Challenge

import pandas as pd

print("="*60)
print("        DAY 31: COMPLETE CHALLENGE")
print("="*60)

# ============================================
# CHALLENGE: E-COMMERCE STORE ANALYTICS
# ============================================

# Store data
orders = {
    'Order_ID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    'Product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Monitor', 'Keyboard', 'Phone'],
    'Price': [50000, 30000, 25000, 50000, 30000, 15000, 5000, 30000],
    'Quantity': [2, 1, 3, 1, 2, 4, 10, 1],
    'Customer_Type': ['Premium', 'Regular', 'Premium', 'Regular', 'Premium', 'Regular', 'Regular', 'Premium']
}

df = pd.DataFrame(orders)

print("\nOriginal Orders:")
print(df)

# ============================================
# STEP 1: Calculate Subtotal
# ============================================

df['Subtotal'] = df['Price'] * df['Quantity']

print("\n--- STEP 1: Subtotal Added ---")
print(df[['Order_ID', 'Product', 'Price', 'Quantity', 'Subtotal']])

# ============================================
# STEP 2: Apply Discount
# ============================================

def calculate_discount(row):
    if row['Customer_Type'] == 'Premium':
        return row['Subtotal'] * 0.10  # 10% discount
    else:
        return 0

df['Discount'] = df.apply(calculate_discount, axis=1)

print("\n--- STEP 2: Discount Applied ---")
print(df[['Order_ID', 'Customer_Type', 'Subtotal', 'Discount']])

# ============================================
# STEP 3: Calculate Tax (7.5%)
# ============================================

df['Tax'] = (df['Subtotal'] - df['Discount']) * 0.075

print("\n--- STEP 3: Tax Calculated ---")
print(df[['Order_ID', 'Subtotal', 'Discount', 'Tax']])

# ============================================
# STEP 4: Final Total
# ============================================

df['Total'] = df['Subtotal'] - df['Discount'] + df['Tax']

print("\n--- STEP 4: Final Total ---")
print(df[['Order_ID', 'Product', 'Total']])

# ============================================
# STEP 5: Analytics
# ============================================

print("\n" + "="*60)
print("        ANALYTICS DASHBOARD")
print("="*60)

# Overall stats
print("\n--- OVERALL STATS ---")
print(f"Total Orders: {len(df)}")
print(f"Total Revenue: ₦{df['Total'].sum():,.2f}")
print(f"Total Discount Given: ₦{df['Discount'].sum():,.2f}")
print(f"Total Tax Collected: ₦{df['Tax'].sum():,.2f}")
print(f"Average Order Value: ₦{df['Total'].mean():,.2f}")

# By customer type
print("\n--- BY CUSTOMER TYPE ---")
for ctype in df['Customer_Type'].unique():
    cust_df = df[df['Customer_Type'] == ctype]
    print(f"\n{ctype} Customers:")
    print(f"  Orders: {len(cust_df)}")
    print(f"  Revenue: ₦{cust_df['Total'].sum():,.2f}")
    print(f"  Avg Order: ₦{cust_df['Total'].mean():,.2f}")

# Top products
print("\n--- TOP PRODUCTS ---")
product_sales = df.groupby('Product')['Total'].sum().sort_values(ascending=False)
print(product_sales)

# ============================================
# STEP 6: Add Performance Categories
# ============================================

def categorize_order(total):
    if total >= 100000:
        return 'High Value'
    elif total >= 50000:
        return 'Medium Value'
    else:
        return 'Low Value'

df['Order_Category'] = df['Total'].apply(categorize_order)

print("\n--- ORDER CATEGORIES ---")
print(df[['Order_ID', 'Total', 'Order_Category']])

# ============================================
# STEP 7: Save Results
# ============================================

print("\n" + "="*60)
print("        SAVING RESULTS")
print("="*60)

df.to_csv('complete_orders.csv', index=False)
print("✅ Saved complete_orders.csv")

# Save summary
summary = df.groupby('Product').agg({
    'Quantity': 'sum',
    'Total': 'sum'
}).round(2)
summary.to_csv('product_summary.csv')
print("✅ Saved product_summary.csv")

print("\n🎉 Day 31 Complete!")
print(f"📊 Processed {len(df)} orders worth ₦{df['Total'].sum():,.2f}")
