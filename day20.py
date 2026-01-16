# Day 20 - Complete Crypto Price Tracker

import requests
import time

print("="*60)
print("         CRYPTO PRICE TRACKER")
print("="*60)

def get_crypto_prices(crypto_ids):
    """Get prices for multiple cryptocurrencies"""
    try:
        # Create URL with crypto IDs
        ids = ",".join(crypto_ids)
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd&include_24hr_change=true"

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ API Error: Status {response.status_code}")
            return None

    except requests.exceptions.Timeout:
        print("❌ Request timed out! Check internet connection.")
        return None
    except requests.exceptions.ConnectionError:
        print("❌ Connection error! Are you online?")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def display_crypto_price(name, symbol, emoji, data):
    """Display one crypto's price nicely"""
    if name.lower() in data:
        crypto_data = data[name.lower()]
        price = crypto_data['usd']
        change = crypto_data['usd_24h_change']

        # Choose emoji based on price movement
        trend = "📈" if change > 0 else "📉"

        # Format differently based on price size
        if price < 1:
            price_str = f"${price:.6f}"
        elif price < 100:
            price_str = f"${price:.2f}"
        else:
            price_str = f"${price:,.2f}"

        print(f"{emoji} {symbol:<6} {price_str:>15}  {trend} {change:+.2f}%")
    else:
        print(f"{emoji} {symbol:<6} {'Not available':>15}")


def quick_check():
    """Quick check of top cryptos"""
    print("\n🌐 Fetching prices from CoinGecko API...\n")

    cryptos = ["bitcoin", "ethereum", "cardano", "solana", "polkadot"]
    data = get_crypto_prices(cryptos)

    if data:
        print("="*60)
        print("            CURRENT CRYPTO PRICES")
        print("="*60)
        print()

        display_crypto_price("bitcoin", "BTC", "💰", data)
        display_crypto_price("ethereum", "ETH", "💎", data)
        display_crypto_price("cardano", "ADA", "🔷", data)
        display_crypto_price("solana", "SOL", "☀️", data)
        display_crypto_price("polkadot", "DOT", "🔴", data)

        print()
        print("="*60)
        print("📈 = UP in 24h  |  📉 = DOWN in 24h")
        print("="*60)


def custom_search():
    """Search for any cryptocurrency"""
    print("\n🔍 SEARCH FOR ANY CRYPTO")
    print()
    print("Examples: bitcoin, ethereum, dogecoin, shiba-inu")
    print("(Use lowercase, use hyphens for multi-word names)")
    print()

    crypto_name = input("Enter crypto name: ").lower().strip()

    if not crypto_name:
        print("❌ Please enter a name!")
        return

    print(f"\n🌐 Searching for {crypto_name}...")

    data = get_crypto_prices([crypto_name])

    if data and crypto_name in data:
        crypto_data = data[crypto_name]
        price = crypto_data['usd']
        change = crypto_data['usd_24h_change']

        trend = "UP 📈" if change > 0 else "DOWN 📉"

        print()
        print("="*60)
        print(f"  {crypto_name.upper()}")
        print("="*60)
        print(f"Price:      ${price:,.6f}")
        print(f"24h Change: {change:+.2f}% {trend}")
        print("="*60)
    else:
        print(f"❌ '{crypto_name}' not found!")
        print("💡 Try: bitcoin, ethereum, cardano, solana")


def save_prices():
    """Save current prices to file"""
    print("\n💾 Saving current prices...")

    cryptos = ["bitcoin", "ethereum", "cardano", "solana"]
    data = get_crypto_prices(cryptos)
    if data:
        try:
            # Get current time
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open("crypto_prices.txt", "a") as file:
                file.write(f"\n--- {timestamp} ---\n")

                for crypto in cryptos:
                    if crypto in data:
                        price = data[crypto]['usd']
                        change = data[crypto]['usd_24h_change']
                        file.write(f"{crypto}: ${price:,.2f} ({change:+.2f}%)\n")

            print("✅ Prices saved to crypto_prices.txt!")
        except Exception as e:
            print(f"❌ Failed to save: {e}")
    else:
        print("❌ Failed to get prices!")

def view_history():
    """View saved price history"""
    print("\n📖 PRICE HISTORY:")

    try:
        with open("crypto_prices.txt", "r") as file:
            content = file.read()

        if content:
            print()
            print(content)
        else:
            print("No history yet! Use 'Save prices' first.")

    except FileNotFoundError:
        print("No history yet! Use 'Save prices' first.")


def live_tracker():
    """Live updating price tracker"""
    print("\n📡 LIVE PRICE TRACKER")
    print("Updates every 60 seconds. Press Ctrl+C to stop.")
    print()

    try:
        count = 0
        while True:
            count += 1
            print(f"\n--- Update #{count} ---")
            quick_check()

            print("\n⏳ Next update in 60 seconds...")
            time.sleep(60)

    except KeyboardInterrupt:
        print("\n\n⏹️ Live tracker stopped!")


# Main menu
while True:
    print("\n" + "="*60)
    print("               CRYPTO TRACKER MENU")
    print("="*60)
    print("1. 📊 Quick price check (Top 5 cryptos)")
    print("2. 🔍 Search any cryptocurrency")
    print("3. 💾 Save current prices")
    print("4. 📖 View price history")
    print("5. 📡 Live tracker (auto-updates)")
    print("6. 🚪 Exit")
    print("="*60)

    choice = input("\nYour choice: ")

    if choice == "1":
        quick_check()

    elif choice == "2":
        custom_search()

    elif choice == "3":
        save_prices()

    elif choice == "4":
        view_history()

    elif choice == "5":
        live_tracker()

    elif choice == "6":
        print("\n" + "="*60)
        print("Thanks for using Crypto Tracker! 💰")
        print("="*60)
        break

    else:
        print("\n❌ Invalid choice! Pick 1-6")
