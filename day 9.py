# Day 9 - Guessing Game (Unlimited Tries)

import random

print("===== NUMBER GUESSING GAME =====")
print("I'm thinking of a number between 1 and 100")
print("Keep guessing until you get it!")
print()

secret_number = random.randint(1, 100)
guess = 0
attempts = 0

while guess != secret_number:
    guess = int(input("Your guess: "))
    attempts = attempts + 1

    if guess < secret_number:
        print("📈 Too low! Try higher.")
    elif guess > secret_number:
        print("📉 Too high! Try lower.")
    else:
        print("🎉 Correct! You got it!")
        print("It took you " + str(attempts) + " attempts.")


# Day 9 - Guessing Game with Hints

import random

print("===== GUESSING GAME WITH HINTS =====")
print()

secret = random.randint(1, 100)
guess = 0
attempts = 0

while guess != secret:
    guess = int(input("Guess (1-100): "))
    attempts = attempts + 1

    if guess == secret:
        print("🎉 CORRECT!")
        print("Attempts: " + str(attempts))
    else:
        difference = abs(secret - guess)

        if difference > 50:
            print("🥶 Ice cold!")
        elif difference > 30:
            print("❄️ Cold!")
        elif difference > 10:
            print("🌡️ Warm!")
        elif difference > 5:
            print("🔥 Hot!")
        else:
            print("🌋 VERY HOT!")

        if guess < secret:
            print("👆 Go higher")
        else:
            print("👇 Go lower")
        print()


# Day 9 - Guessing Game with Replay

import random

play_again = "yes"

while play_again == "yes":
    print("\n===== NEW GAME =====")

    secret = random.randint(1, 50)
    guess = 0
    attempts = 0

    while guess != secret:
        guess = int(input("Guess (1-50): "))
        attempts = attempts + 1

        if guess < secret:
            print("⬆️ Higher!")
        elif guess > secret:
            print("⬇️ Lower!")
        else:
            print("✅ Correct in " + str(attempts) + " tries!")

    play_again = input("\nPlay again? (yes/no): ").lower()

print("Thanks for playing! 👋")


# Day 9 - Guessing Game with Limited Attempts

import random

print("===== GUESSING GAME - 7 ATTEMPTS =====")
print()

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7
won = False

while attempts < max_attempts:
    remaining = max_attempts - attempts
    print("Attempts remaining: " + str(remaining))

    guess = int(input("Your guess: "))
    attempts = attempts + 1

    if guess == secret:
        print("🎉 YOU WIN!")
        print("Got it in " + str(attempts) + " attempts!")
        won = True
        break  # Exit the loop immediately
    elif guess < secret:
        print("📈 Higher!")
    else:
        print("📉 Lower!")
    print()

if not won:
    print("💀 GAME OVER!")
    print("The number was: " + str(secret))


count = 0
while count < 10:
    print(count)
    count = count + 1

answer = ""
while answer != "yes":
    answer = input("Ready? (yes/no): ")

total = 0
while total < 100:
    total = total + random.randint(1, 20)
    print(total)

while True:
    choice = input("Continue? (yes/no): ")
    if choice == "no":
        break  # Exit loopa
