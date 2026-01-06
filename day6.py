#Day6 - Functions

#Exercise 1: Simple function with no parametera
def greet():
    print("Hello!")
    print("Welcome to the functions")

# Call the function
greet()

#Exercise 2: Function with parameters
def greet_person(name):
   print("hello " + name + "!")
   print("Welcome to Python!")

# Call the function with different names
greet_person("Muhammed")
greet_person("Ahmed")
greet_person("Dara")

#Exercise 3: Multiple Parameters
def introduce(name, age, city):
   print("My name is " + name)
   print("I am " + str(age) + " years old")
   print(" i live in " + city)
   print()

# call it 
introduce("Muhammed", 25, "Lagos")
introduce("Ahmed", 34, "Kaduna")



# Exercise 4: functions that return value

# This function CALCULATES and RETURNS a value
def add_numbers(a, b):
          result = a + b
          return result
          
#Store the result
answer = add_numbers(10, 5)
print("10 + 5 = ", str(answer))

#You can use it directly in print
print("28 + 30 =" + str(add_numbers(20, 30)))

def add_numbers(a,b):
    result =a + b
    return result # Sends the value BACK to whoever called it

def add_numbers(a,b):
    result =a + b
    print(result) # Just prints, doesnt give the value back

answer = add_numbers(5, 3)  # answer is None (nothing)

def add_numbers(a,b):
    result =a + b
    return result # Gives the value back

answer = add_numbers(5, 3) # answer is 8 (you can use it)


# Day 6 - Calculator with Functions
# Define all four functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   return a / b

# Test them all
   print("===== CALCULATOR FUNCTIONS =====")
   print()

num1 = 10
num2 = 5

print("Numbers: " + str(num1) + " and " + str(num2))
print()
print("Addition: " + str(add(num1, num2)))
print("Subtraction: " + str(subtract(num1, num2)))
print("Multiplication: " + str(multiply(num1, num2)))
print("Division: " + str(divide(num1, num2)))


# Day 6 - Interactive Calculator with Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Main program
print("===== CALCULATOR =====")
print()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print()
print("===== RESULTS =====")
print("Addition: " + str(add(num1, num2)))
print("Subtraction: " + str(subtract(num1, num2)))
print("Multiplication: " + str(multiply(num1, num2)))
print("Division: " + str(divide(num1, num2)))


# Day 6 - Advanced Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def calculator():
    print("===== CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print()

    choice = input("Choose operation (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print()
    print("===== RESULT =====")

    if choice == "1":
        print(str(num1) + " + " + str(num2) + " = " + str(add(num1, num2)))
    elif choice == "2":
        print(str(num1) + " - " + str(num2) + " = " + str(subtract(num1, num2)))
    elif choice == "3":
        print(str(num1) + " * " + str(num2) + " = " + str(multiply(num1, num2)))
    elif choice == "4":
        print(str(num1) + " / " + str(num2) + " = " + str(divide(num1, num2)))
    else:
        print("Invalid choice!")

# Call the main function
calculator()
