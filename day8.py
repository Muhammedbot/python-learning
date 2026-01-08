# Day 8 - For Loops

# Exercise 1: Basic loop
print("===== COUNTING 1 TO 10 =====")

for i in range(1, 11):
    print(i)

# Exercise 2: Different range patterns

print("\n===== RANGE PATTERNS =====")

# Pattern 1: range(stop) - starts at 0
print("range(5):")
for i in range(5):
    print(i)  # Prints: 0, 1, 2, 3, 4

print()

# Pattern 2: range(start, stop)
print("range(1, 6):")
for i in range(1, 6):
    print(i)  # Prints: 1, 2, 3, 4, 5

print()

# Pattern 3: range(start, stop, step)
print("range(0, 11, 2):")
for i in range(0, 11, 2):
    print(i)  # Prints: 0, 2, 4, 6, 8, 10 (even numbers!)

print()

# Pattern 4: Counting backwards!
print("range(10, 0, -1):")
for i in range(10, 0, -1):
    print(i)  # Prints: 10, 9, 8... 1 (countdown!)

# Exercise 3: Sum of numbers 1 to 100

print("\n===== SUM 1 TO 100 =====")

total = 0  # Start with 0

for i in range(1, 101):
    total = total + i  # Add each number to total

print("The sum of 1 to 100 is: " + str(total))


# Exercise 4: Print patterns

print("\n===== PATTERNS =====")

# Pattern 1: Stars
print("Pattern 1:")
for i in range(5):
    print("*" * (i + 1))

print()

# Pattern 2: Numbers
print("Pattern 2:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # New line after each row

print()

# Pattern 3: Countdown
print("Countdown:")
for i in range(10, 0, -1):
    print(str(i) + "...")
print("BLAST OFF! 🚀")


# Exercise 4: Print patterns

print("\n===== PATTERNS =====")

# Pattern 1: Stars
print("Pattern 1:")
for i in range(5):
    print("*" * (i + 1))

print()

# Pattern 2: Numbers
print("Pattern 2:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # New line after each row

print()

# Pattern 3: Countdown
print("Countdown:")
for i in range(10, 0, -1):
    print(str(i) + "...")
print("BLAST OFF! 🚀")


# Exercise 4: Print patterns

print("\n===== PATTERNS =====")

# Pattern 1: Stars
print("Pattern 1:")
for i in range(5):
    print("*" * (i + 1))

print()

# Pattern 2: Numbers
print("Pattern 2:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # New line after each row

print()

# Pattern 3: Countdown
print("Countdown:")
for i in range(10, 0, -1):
    print(str(i) + "...")
print("BLAST OFF! 🚀")


# Day 8 - Multiplication Tables

print("===== MULTIPLICATION TABLE GENERATOR =====")
print()

# Get the number from user
number = int(input("Which multiplication table? (1-12): "))

print()
print("===== MULTIPLICATION TABLE OF " + str(number) + " =====")

for i in range(1, 13):
    result = number * i
    print(str(number) + " x " + str(i) + " = " + str(result))

# Day 8 - All Multiplication Tables

print("===== ALL MULTIPLICATION TABLES (1-10) =====")
print()

for num in range(1, 11):
    print("Table of " + str(num) + ":")
    for i in range(1, 11):
        result = num * i
        print(str(num) + " x " + str(i) + " = " + str(result))
    print()  # Blank line between tables


# Day 8 - Formatted Multiplication Table

print("===== MULTIPLICATION TABLE =====")
print()

number = int(input("Enter a number (1-20): "))
print()

for i in range(1, 13):
    result = number * i
    # Formatted output (looks cleaner!)
    print(f"{number} x {i:2d} = {result:3d}")


# Day 8 - Multiplication Practice Quiz

import random

print("===== MULTIPLICATION PRACTICE =====")
print("Answer 5 questions!")
print()

score = 0

for question in range(1, 6):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 * num2

    print("Question " + str(question) + ":")
    user_answer = int(input(str(num1) + " x " + str(num2) + " = "))

    if user_answer == correct_answer:
        print("✅ Correct!")
        score = score + 1
    else:
        print("❌ Wrong! Answer is " + str(correct_answer))
    print()

print("===== RESULTS =====")
print("You got " + str(score) + " out of 5 correct!")

if score == 5:
    print("Perfect score! 🎉")
elif score >= 3:
    print("Good job! 👍")
else:
    print("Keep practicing! 💪")


