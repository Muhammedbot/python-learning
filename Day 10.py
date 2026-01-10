# Day 10 - Lists

# Exercise 1: Creating lists
print("===== MY FIRST LIST =====")

# Create a list of friends
friends = ["Ahmed", "Fatima", "Ali", "Aisha", "Omar"]

# Print the entire list
print(friends)

# Print individual items
print("\nMy friends are:")
print(friends[0])  # First friend
print(friends[1])  # Second friend
print(friends[2])  # Third friend


# Exercise 2: Working with lists

print("\n===== LIST OPERATIONS =====")

# Create a list of numbers
numbers = [10, 20, 30, 40, 50]

# Length of list
print("How many numbers? " + str(len(numbers)))

# First and last items
print("First number: " + str(numbers[0]))
print("Last number: " + str(numbers[-1]))

# Add a new number to the end
numbers.append(60)
print("\nAfter adding 60:")
print(numbers)

# Remove a number
numbers.remove(30)
print("\nAfter removing 30:")
print(numbers)

# Insert at specific position
numbers.insert(2, 25)  # Insert 25 at index 2
print("\nAfter inserting 25 at position 2:")
print(numbers)

# Check if item exists
if 40 in numbers:
    print("\n40 is in the list!")



# Exercise 3: Looping through lists

print("\n===== LOOPING THROUGH LISTS =====")

fruits = ["Apple", "Banana", "Orange", "Mango", "Grape"]

# Method 1: Simple loop
print("My fruits:")
for fruit in fruits:
    print("- " + fruit)

print()

# Method 2: Loop with index numbers
print("Numbered list:")
for i in range(len(fruits)):
    print(str(i + 1) + ". " + fruit[i])

print()

# Method 3: Modern way (enumerate)
print("Modern way:")
for index, fruit in enumerate(fruits, 1):
    print(str(index) + ". " + fruit)

# Exercise 4: Math with lists

print("\n===== WORKING WITH NUMBER LISTS =====")

scores = [85, 92, 78, 95, 88, 73, 90]

# Calculate total
total = 0
for score in scores:
    total = total + score

print("Scores: " + str(scores))
print("Total: " + str(total))
print("Average: " + str(total / len(scores)))
print("Highest: " + str(max(scores)))
print("Lowest: " + str(min(scores)))

# Count passing scores (70+)
passing = 0
for score in scores:
    if score >= 70:
        passing = passing + 1

print("Passing students: " + str(passing) + " out of " + str(len(scores)))

# Day10 - To do list app

print("===== TO-DO LIST APP =====")
print()

# Empty list to start
todo_list = []

# Main loop
while True:
    print("\n--- MENU ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

    choice = input("\nChoose (1-5): ")

    if choice == "1":
        # View all tasks
        print("\n===== YOUR TASKS =====")
        if len(todo_list) == 0:
            print("No tasks yet! Add some.")
        else:
            for i in range(len(todo_list)):
                print(str(i + 1) + ". " + todo_list[i])

    elif choice == "2":
        # Add new task
        task = input("\nEnter new task: ")
        todo_list.append(task)
        print("✅ Task added!")

    elif choice == "3":
        # Mark task as complete (remove it)
        if len(todo_list) == 0:
            print("\nNo tasks to complete!")
        else:
            print("\n--- Your Tasks ---")
            for i in range(len(todo_list)):
                print(str(i + 1) + ". " + todo_list[i])

            task_num = int(input("\nWhich task to complete? "))
            if 1 <= task_num <= len(todo_list):
                completed = todo_list.pop(task_num - 1)
                print("✅ Completed: " + completed)
            else:
                print("Invalid task number!")

    elif choice == "4":
        # Delete task
        if len(todo_list) == 0:
            print("\nNo tasks to delete!")
        else:
            print("\n--- Your Tasks ---")
            for i in range(len(todo_list)):
                print(str(i + 1) + ". " + todo_list[i])

            task_num = int(input("\nWhich task to delete? "))
            if 1 <= task_num <= len(todo_list):
                deleted = todo_list.pop(task_num - 1)
                print("🗑️ Deleted: " + deleted)
            else:
                print("Invalid task number!")

    elif choice == "5":
        # Exit
        print("\n👋 Goodbye!")
        break

    else:
        print("\n❌ Invalid choice! Pick 1-5.")


# Day 10 - Shopping List

print("===== SHOPPING LIST =====")

items = []
quantities = []

while True:
    print("\n1. View list")
    print("2. Add item")
    print("3. Remove item")
    print("4. Exit")

    choice = input("\nChoice: ")

    if choice == "1":
        if len(items) == 0:
            print("\nList is empty!")
        else:
            print("\n--- Shopping List ---")
            for i in range(len(items)):
                print(str(i + 1) + ". " + items[i] + " (x" + str(quantities[i]) + ")")

    elif choice == "2":
        item = input("Item name: ")
        qty = int(input("Quantity: "))
        items.append(item)
        quantities.append(qty)
        print("✅ Added!")

    elif choice == "3":
        if len(items) > 0:
            for i in range(len(items)):
                print(str(i + 1) + ". " + items[i])
            num = int(input("Remove which? "))
            if 1 <= num <= len(items):
                items.pop(num - 1)
                quantities.pop(num - 1)
                print("✅ Removed!")

    elif choice == "4":
        break


# Day 10 - Contact List

print("===== CONTACT LIST =====")

names = []
phones = []

while True:
    print("\n1. View contacts")
    print("2. Add contact")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("\nChoice: ")

    if choice == "1":
        if len(names) == 0:
            print("\nNo contacts yet!")
        else:
            print("\n--- Contacts ---")
            for i in range(len(names)):
                print(str(i + 1) + ". " + names[i] + " - " + phones[i])

    elif choice == "2":
        name = input("Name: ")
        phone = input("Phone: ")
        names.append(name)
        phones.append(phone)
        print("✅ Contact saved!")

    elif choice == "3":
        search = input("Search for: ")
        found = False
        for i in range(len(names)):
            if search.lower() in names[i].lower():
                print("Found: " + names[i] + " - " + phones[i])
                found = True
        if not found:
            print("Not found!")

    elif choice == "4":
        if len(names) > 0:
            for i in range(len(names)):
                print(str(i + 1) + ". " + names[i])
            num = int(input("Delete which? "))
            if 1 <= num <= len(names):
                names.pop(num - 1)
                phones.pop(num - 1)
                print("✅ Deleted!")

    elif choice == "5":
        break


# Day 10 - Grade Book

print("===== STUDENT GRADE BOOK =====")

students = []
grades = []

while True:
    print("\n1. View all grades")
    print("2. Add student")
    print("3. Calculate average")
    print("4. Find highest/lowest")
    print("5. Exit")

    choice = input("\nChoice: ")

    if choice == "1":
        if len(students) == 0:
            print("\nNo students yet!")
        else:
            print("\n--- Grade Book ---")
            for i in range(len(students)):
                print(students[i] + ": " + str(grades[i]))

    elif choice == "2":
        name = input("Student name: ")
        grade = int(input("Grade (0-100): "))
        students.append(name)
        grades.append(grade)
        print("✅ Added!")

    elif choice == "3":
        if len(grades) > 0:
            average = sum(grades) / len(grades)
            print("Class average: " + str(round(average, 2)))
        else:
            print("No grades yet!")

    elif choice == "4":
        if len(grades) > 0:
            highest_index = grades.index(max(grades))
            lowest_index = grades.index(min(grades))
            print("Highest: " + students[highest_index] + " - " + str(grades[highest_index]))
            print("Lowest: " + students[lowest_index] + " - " + str(grades[lowest_index]))
        else:
            print("No grades yet!")

    elif choice == "5":
        break


