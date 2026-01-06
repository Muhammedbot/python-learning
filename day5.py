
#Day5 - Grade Calculator

print("===== GRADE CALCULATOR =====")
print()

# Get student's score
print("enter your test score (0-100): ")
score = int(input())

#Check grade
if score >= 90:
    print("Grade: A")
    print("Excellent work!")
elif score >= 80:
    print("Grade: B")
    print("Great job!")
elif score >= 70:
    print("Grade: C")
    print("Good effort!")
elif score >= 60:
    print("Grade: D")
    print("You passed, but study more!")
else:
   print("Grade: F")
   print("Failed, Don't give up, study harder!")


#Day5 - Grade Calculator (Better version)
print("===== GRADE CALCULATOR =====")
print()
# Get student name and score
name = input("Enter Student name: :")
score = int(input("Enter your test score (0-100): "))

print()
print("===== RESULTS =====")
print("Student: " + name)
print("Score: " + str(score) + "/100")

#Calculate grade
if score >= 90:
    grade = "A"
    message = "Outstanding! Keep it up!"
elif score >= 80:
    grade = "B"
    message = "Great work! Almost an A!"
elif score >= 70:
    grade = "C"
    message = "Good job! Room for improve!"
elif score >= 60:
    grade = "D"
    message = "You passed! But you need to study more!"
else:
    grade = "F"
    message = "You Failed! Review the material and try again!"

print("Grade: " + grade)
print("Comment: " + message)

