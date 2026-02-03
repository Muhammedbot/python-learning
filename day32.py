# Day 32 - Complete Grouping & Sorting Challenge

import pandas as pd

print("="*60)
print("        DAY 32: SALES ANALYTICS SYSTEM")
print("="*60)

# ============================================
# COMPREHENSIVE SALES DATA
# ============================================

sales = {
    'Date': ['2026-01-01', '2026-01-01', '2026-01-02', '2026-01-02',
             '2026-01-03', '2026-01-03', '2026-01-04', '2026-01-04',
             '2026-01-05', '2026-01-05', '2026-01-06', '2026-01-06'],
    'City': ['Lagos', 'Abuja', 'Lagos', 'Kano', 'Lagos', 'Abuja',
             'Kano', 'Lagos', 'Abuja', 'Lagos', 'Kano', 'Abuja'],
    'Product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Laptop',
                'Phone', 'Tablet', 'Tablet', 'Laptop', 'Laptop', 'Phone'],
    'Salesperson': ['Ahmed', 'Fatima', 'Ahmed', 'Ibrahim', 'Fatima', 'Ahmed',
                    'Ibrahim', 'Ahmed', 'Fatima', 'Ibrahim', 'Ahmed', 'Fatima'],
    'Quantity': [2, 3, 1, 2, 4, 1, 3, 2, 1, 2, 1, 5],
    'Price': [50000, 30000, 25000, 50000, 30000, 50000, 
              30000, 25000, 25000, 50000, 50000, 30000]
}

df = pd.DataFrame(sales)
df['Total'] = df['Quantity'] * df['Price']

print("\nComplete Sales Data:")
print(df)

# ============================================
# ANALYSIS 1: BY CITY
# ============================================

print("\n" + "="*60)
print("ANALYSIS 1: PERFORMANCE BY CITY")
print("="*60)

city_analysis = df.groupby('City').agg({
    'Total': ['sum', 'mean', 'count'],
    'Quantity': 'sum'
}).round(2)

print(city_analysis)

# Detailed city report
print("\n--- DETAILED CITY REPORT ---")
for city in df['City'].unique():
    city_df = df[df['City'] == city]
    print(f"\n{city}:")
    print(f"  Total Revenue: ₦{city_df['Total'].sum():,}")
    print(f"  Number of Sales: {len(city_df)}")
    print(f"  Average Sale: ₦{city_df['Total'].mean():,.2f}")
    print(f"  Units Sold: {city_df['Quantity'].sum()}")

# ============================================
# ANALYSIS 2: BY PRODUCT
# ============================================

print("\n" + "="*60)
print("ANALYSIS 2: PRODUCT PERFORMANCE")
print("="*60)

product_analysis = df.groupby('Product').agg({
    'Total': 'sum',
    'Quantity': 'sum',
    'Price': 'mean'
}).round(2)

print(product_analysis)

# Sort by revenue
print("\n--- TOP PRODUCTS BY REVENUE ---")
top_products = df.groupby('Product')['Total'].sum().sort_values(ascending=False)
print(top_products)

# ============================================
# ANALYSIS 3: BY SALESPERSON
# ============================================

print("\n" + "="*60)
print("ANALYSIS 3: SALESPERSON PERFORMANCE")
print("="*60)

sales_performance = df.groupby('Salesperson').agg({
    'Total': 'sum',
    'Quantity': 'sum'
}).sort_values('Total', ascending=False)

print(sales_performance)

# Leaderboard
print("\n--- SALES LEADERBOARD ---")
for i, (person, row) in enumerate(sales_performance.iterrows(), 1):
    print(f"{i}. {person}: ₦{row['Total']:,} ({row['Quantity']} units)")

# ============================================
# ANALYSIS 4: MULTI-DIMENSIONAL
# ============================================

print("\n" + "="*60)
print("ANALYSIS 4: CITY × PRODUCT")
print("="*60)

city_product = df.groupby(['City', 'Product'])['Total'].sum().sort_values(ascending=False)
print(city_product)

# As pivot table
print("\n--- PIVOT: CITY vs PRODUCT ---")
pivot = df.pivot_table(
    values='Total',
    index='City',
    columns='Product',
    aggfunc='sum',
    fill_value=0
)
print(pivot)

# ============================================
# ANALYSIS 5: TOP PERFORMERS
# ============================================

print("\n" + "="*60)
print("ANALYSIS 5: TOP PERFORMERS")
print("="*60)

# Highest single sale
top_sale = df.loc[df['Total'].idxmax()]
print(f"\nHighest Single Sale:")
print(f"  Salesperson: {top_sale['Salesperson']}")
print(f"  Product: {top_sale['Product']}")
print(f"  City: {top_sale['City']}")
print(f"  Amount: ₦{top_sale['Total']:,}")

# Best city
best_city = df.groupby('City')['Total'].sum().idxmax()
best_city_total = df.groupby('City')['Total'].sum().max()
print(f"\nBest City: {best_city} (₦{best_city_total:,})")

# Best product
best_product = df.groupby('Product')['Total'].sum().idxmax()
best_product_total = df.groupby('Product')['Total'].sum().max()
print(f"Best Product: {best_product} (₦{best_product_total:,})")

# Best salesperson
best_sales = df.groupby('Salesperson')['Total'].sum().idxmax()
best_sales_total = df.groupby('Salesperson')['Total'].sum().max()
print(f"Best Salesperson: {best_sales} (₦{best_sales_total:,})")

# ============================================
# SAVE REPORTS
# ============================================

print("\n" + "="*60)
print("SAVING REPORTS")
print("="*60)

# Save complete data
df.to_csv('complete_sales.csv', index=False)
print("✅ Saved complete_sales.csv")

# Save city summary
city_summary = df.groupby('City').agg({
    'Total': 'sum',
    'Quantity': 'sum'
}).round(2)
city_summary.to_csv('city_summary.csv')
print("✅ Saved city_summary.csv")

# Save product summary
product_summary = df.groupby('Product').agg({
    'Total': 'sum',
    'Quantity': 'sum'
}).round(2)
product_summary.to_csv('product_summary.csv')
print("✅ Saved product_summary.csv")

print("\n🎉 Day 32 Complete!")
print(f"📊 Total Revenue: ₦{df['Total'].sum():,}")
print(f"📦 Total Units Sold: {df['Quantity'].sum()}")
print(f"📈 Number of Transactions: {len(df)}")
