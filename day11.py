# Day 11 - Student Database

print("===== STUDENT DATABASE =====")

# Empty list to store students
students = []

while True:
    print("\n--- MENU ---")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Update grade")
    print("5. Delete student")
    print("6. Show statistics")
    print("7. Exit")

    choice = input("\nChoice (1-7): ")

    if choice == "1":
        # Add new student
        print("\n--- Add Student ---")
        name = input("Name: ")
        age = int(input("Age: "))
        grade = int(input("Grade (0-100): "))
        course = input("Course: ")

        student = {
            "name": name,
            "age": age,
            "grade": grade,
            "course": course
        }

        students.append(student)
        print("✅ Student added!")

    elif choice == "2":
        # View all students
        if len(students) == 0:
            print("\nNo students in database!")
        else:
            print("\n===== ALL STUDENTS =====")
            for i in range(len(students)):
                s = students[i]
                print(str(i + 1) + ". " + s["name"] + " - " + 
                      str(s["age"]) + " years - " + 
                      "Grade: " + str(s["grade"]) + " - " +
                      s["course"])

    elif choice == "3":
        # Search student
        search_name = input("\nSearch for: ").lower()
        found = False

        for student in students:
            if search_name in student["name"].lower():
                print("\n--- Found ---")
                print("Name: " + student["name"])
                print("Age: " + str(student["age"]))
                print("Grade: " + str(student["grade"]))
                print("Course: " + student["course"])
                found = True

        if not found:
            print("\n❌ Student not found!")

    elif choice == "4":
        # Update grade
        if len(students) == 0:
            print("\nNo students!")
        else:
            print("\n--- Students ---")
            for i in range(len(students)):
                print(str(i + 1) + ". " + students[i]["name"])

            num = int(input("\nWhich student? "))
            if 1 <= num <= len(students):
                new_grade = int(input("New grade: "))
                students[num - 1]["grade"] = new_grade
                print("✅ Grade updated!")
            else:
                print("Invalid number!")

    elif choice == "5":
        # Delete student
        if len(students) == 0:
            print("\nNo students!")
        else:
            print("\n--- Students ---")
            for i in range(len(students)):
                print(str(i + 1) + ". " + students[i]["name"])

            num = int(input("\nDelete which? "))
            if 1 <= num <= len(students):
                deleted = students.pop(num - 1)
                print("🗑️ Deleted: " + deleted["name"])
            else:
                print("Invalid number!")

    elif choice == "6":
        # Statistics
        if len(students) == 0:
            print("\nNo students!")
        else:
            print("\n===== STATISTICS =====")

            # Total students
            print("Total students: " + str(len(students)))

            # Average grade
            total = 0
            for student in students:
                total = total + student["grade"]
            avg = total / len(students)
            print("Average grade: " + str(round(avg, 2)))

            # Highest grade
            highest = students[0]
            for student in students:
                if student["grade"] > highest["grade"]:
                    highest = student
            print("Highest: " + highest["name"] + " (" + str(highest["grade"]) + ")")

            # Lowest grade
            lowest = students[0]
            for student in students:
               if student["grade"] < lowest["grade"]:
                     lowest = student
          print("Lowest: " + lowest["name"] + " (" + str(lowest["grade"]) + ")")

    elif choice == "7":
          print("\n👋 Goodbye!")
    break

else:
print("\n❌ Invalid choice!")
