# Day 4 - conditional statements

# Exercise 1: Check if a number is positive
number = -5
if number > 0:
   print("The number is positive!")
else:
   print("The number is not positive")

# Exercise 2:  check if number is positive
number = -5

if number > 0:
   print("positive")
elif number < 0:
    print("negative")
else:
    print("The number is zero")

# Exercise 3: Check password
password = "python123"

if password == "python123":
    print("Access granted")
else:
    print("Wrong password")

#Exercise 4: Check if old enough to vote
age = 10

if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet")
    print(f"wait for {18- age} more years")


# === MAIN PROJECT: Guessing game ===
import random
print("\n===== NUMBER GUESSING GAME =====")
print("i'm thinking of a number between 1 and 10...")

computer_number = random.randint(1, 10)
user_guess = int(input("what's your guess? "))
if user_guess == computer_number:
    print("correct! you won!")
elif user_guess > computer_number:
    print("too high! the number was " + str(computer_number))
else:
    print("too low! the number was " + str(computer_number))
    
    
