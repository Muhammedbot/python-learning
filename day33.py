# Day 33 - Complete Data Visualization

import matplotlib.pyplot as plt
import pandas as pd

print("="*60)
print("        DAY 33: COMPLETE VISUALIZATION")
print("="*60)

# ============================================
# SAMPLE DATA
# ============================================

# Sales data
sales_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Lagos': [15000, 18000, 22000, 20000, 25000, 28000],
    'Abuja': [12000, 14000, 16000, 15000, 18000, 20000],
    'Kano': [10000, 12000, 14000, 13000, 16000, 18000]
}

df = pd.DataFrame(sales_data)

print("\nSales Data:")
print(df)

# ============================================
# CHART 1: Multi-Line Chart
# ============================================

print("\n--- Creating Multi-Line Chart ---")

plt.figure(figsize=(12, 6))
plt.plot(df['Month'], df['Lagos'], marker='o', label='Lagos', linewidth=2)
plt.plot(df['Month'], df['Abuja'], marker='s', label='Abuja', linewidth=2)
plt.plot(df['Month'], df['Kano'], marker='^', label='Kano', linewidth=2)

plt.title('Monthly Sales by City', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales (₦)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig('multi_line_chart.png', dpi=300, bbox_inches='tight')
print("✅ Saved multi_line_chart.png")
plt.close()

# ============================================
# CHART 2: Stacked Bar Chart
# ============================================

print("--- Creating Stacked Bar Chart ---")

months = df['Month']
lagos = df['Lagos']
abuja = df['Abuja']
kano = df['Kano']

plt.figure(figsize=(12, 6))
plt.bar(months, lagos, label='Lagos', color='#FF6B6B')
plt.bar(months, abuja, bottom=lagos, label='Abuja', color='#4ECDC4')
plt.bar(months, kano, bottom=lagos+abuja, label='Kano', color='#45B7D1')

plt.title('Total Sales (Stacked)', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales (₦)', fontsize=12)
plt.legend()

plt.savefig('stacked_bar.png', dpi=300, bbox_inches='tight')
print("✅ Saved stacked_bar.png")
plt.close()

# ============================================
# CHART 3: Performance Comparison
# ============================================

print("--- Creating Comparison Chart ---")

# Total sales per city
city_totals = {
    'Lagos': df['Lagos'].sum(),
    'Abuja': df['Abuja'].sum(),
    'Kano': df['Kano'].sum()
}

plt.figure(figsize=(10, 6))
cities = list(city_totals.keys())
totals = list(city_totals.values())

bars = plt.bar(cities, totals, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'₦{int(height):,}',
             ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.title('Total Sales by City (6 Months)', fontsize=16, fontweight='bold')
plt.ylabel('Total Sales (₦)', fontsize=12)
plt.grid(axis='y', alpha=0.3)

plt.savefig('total_comparison.png', dpi=300, bbox_inches='tight')
print("✅ Saved total_comparison.png")
plt.close()

# ============================================
# CHART 4: Growth Analysis
# ============================================

print("--- Creating Growth Chart ---")

# Calculate month-over-month growth for Lagos
lagos_sales = df['Lagos'].tolist()
growth_rates = []

for i in range(1, len(lagos_sales)):
    growth = ((lagos_sales[i] - lagos_sales[i-1]) / lagos_sales[i-1]) * 100
    growth_rates.append(growth)

growth_months = df['Month'][1:].tolist()

plt.figure(figsize=(10, 6))
colors = ['green' if x > 0 else 'red' for x in growth_rates]
plt.bar(growth_months, growth_rates, color=colors, alpha=0.7)

plt.title('Lagos Month-over-Month Growth Rate', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Growth Rate (%)', fontsize=12)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
plt.grid(axis='y', alpha=0.3)

# Add percentage labels
for i, (month, rate) in enumerate(zip(growth_months, growth_rates)):
    plt.text(i, rate, f'{rate:.1f}%', ha='center', 
             va='bottom' if rate > 0 else 'top', fontsize=10)

plt.savefig('growth_analysis.png', dpi=300, bbox_inches='tight')
print("✅ Saved growth_analysis.png")
plt.close()

# ============================================
# SUMMARY
# ============================================

print("\n" + "="*60)
print("VISUALIZATION COMPLETE!")
print("="*60)
print("\nCreated 4 professional charts:")
print("1. ✅ multi_line_chart.png - Trend comparison")
print("2. ✅ stacked_bar.png - Total breakdown")
print("3. ✅ total_comparison.png - City performance")
print("4. ✅ growth_analysis.png - Growth rates")

print("\n🎨 All charts saved as high-quality PNG files!")
print("📊 Check your files to see the visualizations!")

print("\n🎉 Day 33 Complete!")
