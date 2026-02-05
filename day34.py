# Day 34 - Complete Visualization Practice

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("="*70)
print("        DAY 34: STUDENT PERFORMANCE ANALYSIS")
print("="*70)

# ============================================
# CREATE REALISTIC STUDENT DATA
# ============================================

print("\n📊 Generating student performance data...")

np.random.seed(42)  # For consistent results

# Generate 50 students
students = []
for i in range(50):
    student = {
        'Student_ID': f'S{i+1:03d}',
        'Name': f'Student_{i+1}',
        'Class': np.random.choice(['A', 'B', 'C']),
        'Math': np.random.randint(50, 100),
        'English': np.random.randint(50, 100),
        'Science': np.random.randint(50, 100),
        'Attendance': np.random.randint(70, 100),
        'Study_Hours': np.random.randint(1, 10)
    }
    students.append(student)

df = pd.DataFrame(students)

# Calculate average score
df['Average'] = df[['Math', 'English', 'Science']].mean(axis=1).round(2)

# Assign grades
def get_grade(avg):
    if avg >= 90: return 'A'
    elif avg >= 80: return 'B'
    elif avg >= 70: return 'C'
    elif avg >= 60: return 'D'
    else: return 'F'

df['Grade'] = df['Average'].apply(get_grade)

print(f"✅ Generated data for {len(df)} students")
print("\nSample Data:")
print(df.head(10))

# Save data
df.to_csv('student_data.csv', index=False)
print("\n✅ Saved student_data.csv")

# ============================================
# VISUALIZATION 1: Grade Distribution (Pie Chart)
# ============================================

print("\n📊 Creating Visualization 1: Grade Distribution...")

plt.figure(figsize=(10, 8))

grade_counts = df['Grade'].value_counts().sort_index()
colors = ['#2ecc71', '#3498db', '#f39c12', '#e74c3c', '#95a5a6']
explode = (0.1, 0.05, 0, 0, 0)  # Explode top grades

plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%',
        colors=colors, explode=explode, shadow=True, startangle=90)
plt.title('Grade Distribution\n(50 Students)', fontsize=16, fontweight='bold')

plt.savefig('viz1_grade_distribution.png', dpi=300, bbox_inches='tight')
print("✅ Saved viz1_grade_distribution.png")
plt.close()

# ============================================
# VISUALIZATION 2: Subject Performance (Bar Chart)
# ============================================

print("📊 Creating Visualization 2: Subject Performance...")

plt.figure(figsize=(12, 6))

subjects = ['Math', 'English', 'Science']
averages = [df['Math'].mean(), df['English'].mean(), df['Science'].mean()]
colors_bar = ['#e74c3c', '#3498db', '#2ecc71']

bars = plt.bar(subjects, averages, color=colors_bar, alpha=0.8, edgecolor='black')

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}',
             ha='center', va='bottom', fontsize=14, fontweight='bold')

plt.title('Average Score by Subject', fontsize=16, fontweight='bold')
plt.ylabel('Average Score', fontsize=12)
plt.ylim(0, 100)
plt.grid(axis='y', alpha=0.3)

plt.savefig('viz2_subject_performance.png', dpi=300, bbox_inches='tight')
print("✅ Saved viz2_subject_performance.png")
plt.close()

# ============================================
# VISUALIZATION 3: Class Comparison (Grouped Bar)
# ============================================

print("📊 Creating Visualization 3: Class Comparison...")

plt.figure(figsize=(12, 7))

classes = df['Class'].unique()
x = np.arange(len(subjects))
width = 0.25

for i, cls in enumerate(sorted(classes)):
    class_df = df[df['Class'] == cls]
    scores = [class_df['Math'].mean(), 
              class_df['English'].mean(), 
              class_df['Science'].mean()]
    plt.bar(x + i*width, scores, width, label=f'Class {cls}', alpha=0.8)

plt.xlabel('Subject', fontsize=12)
plt.ylabel('Average Score', fontsize=12)
plt.title('Subject Performance by Class', fontsize=16, fontweight='bold')
plt.xticks(x + width, subjects)
plt.legend()
plt.grid(axis='y', alpha=0.3)

plt.savefig('viz3_class_comparison.png', dpi=300, bbox_inches='tight')
print("✅ Saved viz3_class_comparison.png")
plt.close()

# ============================================
# VISUALIZATION 4: Study Hours vs Performance (Scatter)
# ============================================

print("📊 Creating Visualization 4: Study Hours Impact...")

plt.figure(figsize=(12, 7))

# Color by grade
grade_colors = {'A': '#2ecc71', 'B': '#3498db', 'C': '#f39c12', 
                'D': '#e74c3c', 'F': '#95a5a6'}
colors_scatter = [grade_colors[g] for g in df['Grade']]

plt.scatter(df['Study_Hours'], df['Average'], 
           c=colors_scatter, s=100, alpha=0.6, edgecolors='black')

# Add trend line
z = np.polyfit(df['Study_Hours'], df['Average'], 1)
p = np.poly1d(z)
plt.plot(df['Study_Hours'], p(df['Study_Hours']), 
         "r--", alpha=0.8, linewidth=2, label='Trend')

plt.xlabel('Study Hours per Day', fontsize=12)
plt.ylabel('Average Score', fontsize=12)
plt.title('Study Hours vs Academic Performance', fontsize=16, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend()

# Add grade legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=grade_colors[g], label=f'Grade {g}') 
                   for g in sorted(grade_colors.keys())]
plt.legend(handles=legend_elements, title='Grades', loc='lower right')

plt.savefig('viz4_study_hours_impact.png', dpi=300, bbox_inches='tight')
print("✅ Saved viz4_study_hours_impact.png")
plt.close()

# ============================================
# VISUALIZATION 5: Attendance Impact (Box Plot Style)
# ============================================

print("📊 Creating Visualization 5: Attendance Analysis...")

plt.figure(figsize=(12, 7))

# Categorize attendance
def attendance_category(att):
    if att >= 90: return 'Excellent (90%+)'
    elif att >= 80: return 'Good (80-89%)'
    else: return 'Poor (<80%)'

df['Attendance_Category'] = df['Attendance'].apply(attendance_category)

categories = ['Excellent (90%+)', 'Good (80-89%)', 'Poor (<80%)']
averages_by_attendance = []

for cat in categories:
    cat_df = df[df['Attendance_Category'] == cat]
    if len(cat_df) > 0:
        averages_by_attendance.append(cat_df['Average'].mean())
    else:
        averages_by_attendance.append(0)

colors_att = ['#2ecc71', '#f39c12', '#e74c3c']
bars = plt.bar(categories, averages_by_attendance, color=colors_att, alpha=0.8)

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}',
             ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.ylabel('Average Score', fontsize=12)
plt.title('Impact of Attendance on Performance', fontsize=16, fontweight='bold')
plt.xticks(rotation=15)
plt.grid(axis='y', alpha=0.3)

plt.savefig('viz5_attendance_impact.png', dpi=300, bbox_inches='tight')
print("✅ Saved viz5_attendance_impact.png")
plt.close()

# ============================================
# VISUALIZATION 6: Complete Dashboard
# ============================================

print("📊 Creating Visualization 6: Complete Dashboard...")

fig = plt.figure(figsize=(18, 12))
fig.suptitle('STUDENT PERFORMANCE DASHBOARD', fontsize=24, fontweight='bold', y=0.98)

# Chart 1: Top 10 Students
ax1 = plt.subplot(2, 3, 1)
top10 = df.nlargest(10, 'Average')[['Name', 'Average']].sort_values('Average')
ax1.barh(range(len(top10)), top10['Average'], color='#3498db')
ax1.set_yticks(range(len(top10)))
ax1.set_yticklabels(top10['Name'], fontsize=8)
ax1.set_xlabel('Average Score')
ax1.set_title('Top 10 Students', fontweight='bold')
ax1.grid(axis='x', alpha=0.3)

# Chart 2: Grade Distribution
ax2 = plt.subplot(2, 3, 2)
grade_counts.plot(kind='bar', ax=ax2, color=colors, alpha=0.8)
ax2.set_title('Grade Distribution', fontweight='bold')
ax2.set_xlabel('Grade')
ax2.set_ylabel('Number of Students')
ax2.set_xticklabels(grade_counts.index, rotation=0)

# Chart 3: Subject Averages
ax3 = plt.subplot(2, 3, 3)
ax3.bar(subjects, averages, color=colors_bar, alpha=0.8)
ax3.set_title('Subject Averages', fontweight='bold')
ax3.set_ylabel('Average Score')
ax3.set_ylim(0, 100)
ax3.grid(axis='y', alpha=0.3)

# Chart 4: Class Performance
ax4 = plt.subplot(2, 3, 4)
class_avgs = df.groupby('Class')['Average'].mean().sort_values(ascending=False)
ax4.bar(class_avgs.index, class_avgs.values, color='#2ecc71', alpha=0.8)
ax4.set_title('Average by Class', fontweight='bold')
ax4.set_ylabel('Average Score')
ax4.grid(axis='y', alpha=0.3)

# Chart 5: Performance Distribution
ax5 = plt.subplot(2, 3, 5)
ax5.hist(df['Average'], bins=10, color='#9b59b6', alpha=0.7, edgecolor='black')
ax5.set_title('Score Distribution', fontweight='bold')
ax5.set_xlabel('Average Score')
ax5.set_ylabel('Number of Students')
ax5.grid(axis='y', alpha=0.3)

# Chart 6: Key Statistics (Text)
ax6 = plt.subplot(2, 3, 6)
ax6.axis('off')

stats_text = f"""
KEY STATISTICS

Total Students: {len(df)}

Overall Average: {df['Average'].mean():.2f}
Highest Score: {df['Average'].max():.2f}
Lowest Score: {df['Average'].min():.2f}

Grade A: {len(df[df['Grade']=='A'])} students
Grade B: {len(df[df['Grade']=='B'])} students
Grade C: {len(df[df['Grade']=='C'])} students

Best Subject: {subjects[averages.index(max(averages))]}
Avg Study Hours: {df['Study_Hours'].mean():.1f}
Avg Attendance: {df['Attendance'].mean():.1f}%
"""

ax6.text(0.1, 0.5, stats_text, fontsize=12, family='monospace',
         verticalalignment='center')

plt.tight_layout()
plt.savefig('viz6_complete_dashboard.png', dpi=300, bbox_inches='tight')
print("✅ Saved viz6_complete_dashboard.png")
plt.close()

# ============================================
# GENERATE INSIGHTS REPORT
# ============================================

print("\n" + "="*70)
print("        DATA INSIGHTS & FINDINGS")
print("="*70)

print("\n📊 OVERALL PERFORMANCE:")
print(f"   • Total Students Analyzed: {len(df)}")
print(f"   • Overall Average Score: {df['Average'].mean():.2f}/100")
print(f"   • Standard Deviation: {df['Average'].std():.2f}")

print("\n🎯 GRADE DISTRIBUTION:")
for grade in sorted(df['Grade'].unique()):
    count = len(df[df['Grade'] == grade])
    percentage = (count / len(df)) * 100
    print(f"   • Grade {grade}: {count} students ({percentage:.1f}%)")

print("\n📚 SUBJECT ANALYSIS:")
for i, subject in enumerate(subjects):
    print(f"   • {subject}: {averages[i]:.2f} average")

print("\n👥 CLASS PERFORMANCE:")
for cls in sorted(df['Class'].unique()):
    class_avg = df[df['Class'] == cls]['Average'].mean()
    print(f"   • Class {cls}: {class_avg:.2f} average")

print("\n⏰ STUDY HOURS INSIGHT:")
high_study = df[df['Study_Hours'] >= 6]['Average'].mean()
low_study = df[df['Study_Hours'] < 6]['Average'].mean()
print(f"   • Students studying 6+ hrs/day: {high_study:.2f} avg")
print(f"   • Students studying <6 hrs/day: {low_study:.2f} avg")
print(f"   • Difference: {high_study - low_study:.2f} points")

print("\n📅 ATTENDANCE INSIGHT:")
for cat in categories:
    cat_df = df[df['Attendance_Category'] == cat]
    if len(cat_df) > 0:
        print(f"   • {cat}: {cat_df['Average'].mean():.2f} avg ({len(cat_df)} students)")

print("\n🏆 TOP PERFORMERS:")
top5 = df.nlargest(5, 'Average')
for i, (idx, student) in enumerate(top5.iterrows(), 1):
    print(f"   {i}. {student['Name']}: {student['Average']:.2f} (Grade {student['Grade']})")

print("\n" + "="*70)
print("        ALL VISUALIZATIONS CREATED!")
print("="*70)

print("\n✅ Created 6 visualizations:")
print("   1. viz1_grade_distribution.png - Pie chart of grades")
print("   2. viz2_subject_performance.png - Subject averages")
print("   3. viz3_class_comparison.png - Class comparison")
print("   4. viz4_study_hours_impact.png - Study hours correlation")
print("   5. viz5_attendance_impact.png - Attendance impact")
print("   6. viz6_complete_dashboard.png - Complete overview")

print("\n📁 Also created:")
print("   • student_data.csv - Full dataset")

print("\n🎉 Day 34 Complete!")
print("📊 Professional data analysis with beautiful visualizations!")
