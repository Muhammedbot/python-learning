# Day 7 - Temperature Converter

# Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Celsius to Kelvin
def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

# Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

# Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin

# Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit


# Day 7 - Temperature Converter

# [Keep all your functions from above here]

# Main program
def temperature_converter():
    print("===== TEMPERATURE CONVERTER =====")
    print()
    print("Choose conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print()

    choice = input("Enter choice (1-6): ")
    temperature = float(input("Enter temperature: "))

    print()
    print("===== RESULT =====")

    if choice == "1":
        result = celsius_to_fahrenheit(temperature)
        print(str(temperature) + "°C = " + str(result) + "°F")
    elif choice == "2":
        result = fahrenheit_to_celsius(temperature)
        print(str(temperature) + "°F = " + str(result) + "°C")
    elif choice == "3":
        result = celsius_to_kelvin(temperature)
        print(str(temperature) + "°C = " + str(result) + "K")
    elif choice == "4":
        result = kelvin_to_celsius(temperature)
        print(str(temperature) + "K = " + str(result) + "°C")
    elif choice == "5":
        result = fahrenheit_to_kelvin(temperature)
        print(str(temperature) + "°F = " + str(result) + "K")
    elif choice == "6":
        result = kelvin_to_fahrenheit(temperature)
        print(str(temperature) + "K = " + str(result) + "°F")
    else:
        print("Invalid choice!")

# Run the converter
temperature_converter()

def get_temperature():
    while True:
        try:
            temp = float(input("Enter temperature: "))
            return temp
        except:
            print("Please enter a valid number!")


while True:
    temperature_converter()
    print()
    again = input("Convert another? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye!")
        break


result = celsius_to_fahrenheit(100)
print(f"{100:.1f}°C = {result:.1f}°F")  # Shows: 100.0°C = 212.0°F

print("Fun Facts:")
print("• Water freezes at 0°C = 32°F = 273.15K")
print("• Water boils at 100°C = 212°F = 373.15K")
print("• Room temperature: ~20°C = 68°F = 293.15K")
print("• Body temperature: 37°C = 98.6°F = 310.15K")
