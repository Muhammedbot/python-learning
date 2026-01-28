# Day 30 - Advanced Pandas Selection

import pandas as pd

print("="*60)
print("        DAY 30: ADVANCED SELECTION")
print("="*60)

# Create comprehensive student data
students = {
    'Name': ['Ahmed', 'Fatima', 'Ibrahim', 'Aisha', 'Yusuf', 
             'Maryam', 'Hassan', 'Zainab', 'Omar', 'Khadija'],
    'Age': [23, 25, 22, 24, 26, 21, 23, 27, 24, 22],
    'City': ['Lagos', 'Abuja', 'Lagos', 'Kano', 'Lagos', 
             'Ibadan', 'Lagos', 'Kano', 'Abuja', 'Lagos'],
    'Math': [85, 92, 78, 88, 95, 80, 87, 90, 82, 94],
    'English': [78, 85, 92, 80, 88, 90, 84, 87, 89, 91],
    'Science': [90, 88, 85, 92, 90, 88, 86, 93, 88, 92]
}

df = pd.DataFrame(students)

print("\nFull Student Database:")
print(df)

# ============================================
# CHALLENGE 1: Top Performers
# ============================================

print("\n" + "="*60)
print("CHALLENGE 1: Top Math Students (Score > 90)")
print("="*60)

top_math = df[df['Math'] > 90]
print(top_math[['Name', 'Math']])
print(f"Total: {len(top_math)} students")

# ============================================
# CHALLENGE 2: Lagos Students
# ============================================

print("\n" + "="*60)
print("CHALLENGE 2: All Students from Lagos")
print("="*60)

lagos = df[df['City'] == 'Lagos']
print(lagos[['Name', 'City', 'Math']])
print(f"Total: {len(lagos)} students in Lagos")

# ============================================
# CHALLENGE 3: Excellence (All subjects > 85)
# ============================================

print("\n" + "="*60)
print("CHALLENGE 3: Excellence (All subjects > 85)")
print("="*60)

excellent = df[(df['Math'] > 85) & (df['English'] > 85) & (df['Science'] > 85)]
print(excellent[['Name', 'Math', 'English', 'Science']])
print(f"Total: {len(excellent)} excellent students")

# ============================================
# CHALLENGE 4: Need Help (Any subject < 85)
# ============================================

print("\n" + "="*60)
print("CHALLENGE 4: Students Who Need Extra Help")
print("="*60)

need_help = df[(df['Math'] < 85) | (df['English'] < 85) | (df['Science'] < 85)]
print(need_help[['Name', 'Math', 'English', 'Science']])

# ============================================
# CHALLENGE 5: Top 5 by Average
# ============================================

print("\n" + "="*60)
print("CHALLENGE 5: Top 5 Students by Average")
print("="*60)

df['Average'] = (df['Math'] + df['English'] + df['Science']) / 3
df['Average'] = df['Average'].round(2)

top5 = df.sort_values('Average', ascending=False).head(5)
print(top5[['Name', 'Average']])

# ============================================
# CHALLENGE 6: City Statistics
# ============================================

print("\n" + "="*60)
print("CHALLENGE 6: Average Math Score by City")
print("="*60)

for city in df['City'].unique():
    city_students = df[df['City'] == city]
    avg_math = city_students['Math'].mean()
    print(f"{city}: {avg_math:.2f} average")

# ============================================
# SAVE RESULTS
# ============================================

print("\n" + "="*60)
print("SAVING RESULTS")
print("="*60)

# Save top performers
top_math.to_csv('top_math_students.csv', index=False)
print("✅ Saved top_math_students.csv")

# Save Lagos students
lagos.to_csv('lagos_students.csv', index=False)
print("✅ Saved lagos_students.csv")

# Save complete data with averages
df.to_csv('all_students_with_averages.csv', index=False)
print("✅ Saved all_students_with_averages.csv")

print("\n🎉 Day 30 Complete!")
