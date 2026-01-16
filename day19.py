# Day 19 - My First API Call

import requests

print("Getting a joke from the internet...")
print()

# Ask the internet for a joke
response = requests.get("https://official-joke-api.appspot.com/random_joke")

# Did it work?
if response.status_code == 200:
    print("✅ Success! Got data from internet!")
    print()

    # Get the joke data
    joke = response.json()

    # Show the joke
    print("SETUP:", joke['setup'])
    input("\nPress Enter for punchline...")
    print("PUNCHLINE:", joke['punchline'])
    print()
    print("😂" * 10)
else:
    print("❌ Failed! Status code:", response.status_code)


# Day 19 - Joke App (Step 3: Multiple Jokes)

import requests

print("="*50)
print("       WELCOME TO JOKE APP!")
print("="*50)

while True:
    print("\n--- MENU ---")
    print("1. Get 1 random joke")
    print("2. Get 5 random jokes")
    print("3. Exit")

    choice = input("\nYour choice: ")

    if choice == "1":
        # Get ONE joke
        print("\n🌐 Getting joke from internet...")

        response = requests.get("https://official-joke-api.appspot.com/random_joke")

        if response.status_code == 200:
            joke = response.json()

            print("\n" + "="*50)
            print("😂 JOKE TIME!")
            print("="*50)
            print(f"\n{joke['setup']}")
            input("\nPress Enter for punchline...")
            print(f"👉 {joke['punchline']}")
            print("\n" + "="*50)
        else:
            print("❌ Failed to get joke!")

    elif choice == "2":
        # Get FIVE jokes
        print("\n🌐 Getting 5 jokes from internet...")

        response = requests.get("https://official-joke-api.appspot.com/jokes/ten")

        if response.status_code == 200:
            jokes = response.json()  # This is a LIST of jokes!

            print(f"\n✅ Got {len(jokes)} jokes!")

            # Show first 5 jokes
            for i in range(5):
                joke = jokes[i]
                print(f"\n--- Joke {i+1} ---")
                print(f"Setup: {joke['setup']}")
                print(f"Punchline: {joke['punchline']}")
        else:
            print("❌ Failed to get jokes!")

    elif choice == "3":
        print("\n👋 Thanks for laughing! Goodbye!")
        break

    else:
        print("\n❌ Invalid choice! Pick 1, 2, or 3")a
