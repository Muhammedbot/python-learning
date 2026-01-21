# Day 25 - Weather API - Live Data from Anywhere!

import requests
from datetime import datetime

print("="*70)
print("         WEATHER DASHBOARD - LIVE DATA")
print("="*70)

# API Configuration
API_KEY = "bd5e378503939ddaee76f12ad7a97608"  # Demo key 
BASE_URL = "http://api.openweathermap.org/data/2.5"

# Favorite cities storage
favorite_cities = []


# ============================================
# PROJECT 1: CURRENT WEATHER
# ============================================

def get_current_weather():
    """Get current weather for any city"""
    print("\n" + "="*70)
    print("PROJECT 1: CURRENT WEATHER")
    print("="*70)

    city = input("\nEnter city name (e.g., Lagos, London, New York): ").strip()

    if not city:
        print("❌ City name cannot be empty!")
        return

    print(f"\n🌐 Fetching weather for {city}...")

    try:
        # API endpoint for current weather
        url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            # Extract data
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            temp_min = data['main']['temp_min']
            temp_max = data['main']['temp_max']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            description = data['weather'][0]['description']
            wind_speed = data['wind']['speed']
            country = data['sys']['country']

            # Convert to Fahrenheit
            temp_f = (temp * 9/5) + 32
            feels_f = (feels_like * 9/5) + 32

            # Display weather
            print("\n" + "="*70)
            print(f"🌍 {city.upper()}, {country}")
            print("="*70)
            print(f"🌡️  Temperature: {temp}°C ({temp_f:.1f}°F)")
            print(f"🤔 Feels like: {feels_like}°C ({feels_f:.1f}°F)")
            print(f"📊 Min/Max: {temp_min}°C / {temp_max}°C")
            print(f"☁️  Conditions: {description.title()}")
            print(f"💧 Humidity: {humidity}%")
            print(f"🌬️  Wind Speed: {wind_speed} m/s")
            print(f"🔽 Pressure: {pressure} hPa")
            print("="*70)

            # Save to favorites option
            save = input("\n💾 Save this city to favorites? (yes/no): ").lower()
            if save == "yes":
                if city not in favorite_cities:
                    favorite_cities.append(city)
                    print(f"✅ {city} added to favorites!")
                else:
                    print(f"⚠️ {city} already in favorites!")

        elif response.status_code == 404:
            print(f"❌ City '{city}' not found! Check spelling.")

        elif response.status_code == 401:
            print("❌ Invalid API key! Please check your API key.")

        else:
            print(f"❌ Error: Status code {response.status_code}")

    except requests.exceptions.Timeout:
        print("❌ Request timed out! Check internet connection.")

    except requests.exceptions.ConnectionError:
        print("❌ Connection error! Are you online?")

    except Exception as e:
        print(f"❌ Error: {e}")


# ============================================
# PROJECT 2: 5-DAY FORECAST
# ============================================

def get_forecast():
    """Get 5-day weather forecast"""
    print("\n" + "="*70)
    print("PROJECT 2: 5-DAY FORECAST")
    print("="*70)

    city = input("\nEnter city name: ").strip()

    if not city:
        print("❌ City name cannot be empty!")
        return

    print(f"\n🌐 Fetching 5-day forecast for {city}...")

    try:
        # API endpoint for forecast
        url = f"{BASE_URL}/forecast?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            print("\n" + "="*70)
            print(f"📅 5-DAY FORECAST: {city.upper()}")
            print("="*70)

            # Process forecast (every 3 hours, we'll show daily summary)
            forecasts = data['list']

            # Group by day
            daily_forecasts = {}

            for forecast in forecasts:
                # Get date
                dt = datetime.fromtimestamp(forecast['dt'])
                date_key = dt.strftime('%Y-%m-%d')
                day_name = dt.strftime('%A')

                if date_key not in daily_forecasts:
                    daily_forecasts[date_key] = {
                        'day': day_name,
                        'temps': [],
                        'conditions': [],
                        'humidity': []
                    }

                daily_forecasts[date_key]['temps'].append(forecast['main']['temp'])
                daily_forecasts[date_key]['conditions'].append(forecast['weather'][0]['description'])
                daily_forecasts[date_key]['humidity'].append(forecast['main']['humidity'])

            # Show daily summaries
            count = 0
            for date, info in sorted(daily_forecasts.items())[:5]:
                count += 1
                avg_temp = sum(info['temps']) / len(info['temps'])
                max_temp = max(info['temps'])
                min_temp = min(info['temps'])
                avg_humidity = sum(info['humidity']) / len(info['humidity'])

                # Most common condition
                most_common = max(set(info['conditions']), key=info['conditions'].count)

                print(f"\n📅 Day {count}: {info['day']}, {date}")
                print(f"   🌡️  Avg: {avg_temp:.1f}°C | Min: {min_temp:.1f}°C | Max: {max_temp:.1f}°C")
                print(f"   ☁️  Conditions: {most_common.title()}")
                print(f"   💧 Humidity: {avg_humidity:.0f}%")

            print("\n" + "="*70)

        elif response.status_code == 404:
            print(f"❌ City '{city}' not found!")

        else:
            print(f"❌ Error: Status code {response.status_code}")

    except Exception as e:
        print(f"❌ Error: {e}")


# ============================================
# PROJECT 3: MULTIPLE CITIES COMPARISON
# ============================================

def compare_cities():
    """Compare weather in multiple cities"""
    print("\n" + "="*70)
    print("PROJECT 3: COMPARE MULTIPLE CITIES")
    print("="*70)

    cities = []

    print("\nEnter cities to compare (type 'done' when finished):")

    while len(cities) < 5:
        city = input(f"City {len(cities) + 1} (or 'done'): ").strip()

        if city.lower() == 'done':
            break

        if city:
            cities.append(city)

    if len(cities) < 2:
        print("❌ Need at least 2 cities to compare!")
        return

    print(f"\n🌐 Fetching weather for {len(cities)} cities...")
    print("\n" + "="*70)
    print("WEATHER COMPARISON")
    print("="*70)

    results = []

    for city in cities:
        try:
            url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()

                results.append({
                    'city': city,
                    'temp': data['main']['temp'],
                    'feels_like': data['main']['feels_like'],
                    'conditions': data['weather'][0]['description'],
                    'humidity': data['main']['humidity']
                })

        except:
            print(f"⚠️ Failed to get data for {city}")

    if not results:
        print("❌ No weather data retrieved!")
        return

    # Display comparison
    print()
    for result in results:
        print(f"📍 {result['city'].upper()}")
        print(f"   🌡️  {result['temp']}°C (feels like {result['feels_like']}°C)")
        print(f"   ☁️  {result['conditions'].title()}")
        print(f"   💧 {result['humidity']}% humidity")
        print()

    # Find hottest and coldest
    hottest = max(results, key=lambda x: x['temp'])
    coldest = min(results, key=lambda x: x['temp'])

    print("-"*70)
    print(f"🔥 Hottest: {hottest['city']} ({hottest['temp']}°C)")
    print(f"❄️  Coldest: {coldest['city']} ({coldest['temp']}°C)")
    print("="*70)


# ============================================
# PROJECT 4: FAVORITE CITIES DASHBOARD
# ============================================

def favorites_dashboard():
    """Quick weather for favorite cities"""
    print("\n" + "="*70)
    print("PROJECT 4: FAVORITES DASHBOARD")
    print("="*70)

    if not favorite_cities:
        print("\n❌ No favorite cities yet!")
        print("💡 Use 'Current Weather' and save cities to favorites!")
        return

    print(f"\n🌐 Fetching weather for {len(favorite_cities)} favorite cities...")
    print("\n" + "="*70)
    print("YOUR FAVORITES")
    print("="*70)

    for city in favorite_cities:
        try:
            url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                data = response.json()

                temp = data['main']['temp']
                conditions = data['weather'][0]['description']

                print(f"\n📍 {city.upper()}: {temp}°C - {conditions.title()}")

        except:
            print(f"⚠️ Failed to get data for {city}")

    print("\n" + "="*70)


# ============================================
# PROJECT 5: WEATHER SEARCH BY COORDINATES
# ============================================

def weather_by_coordinates():
    """Get weather by latitude and longitude"""
    print("\n" + "="*70)
    print("PROJECT 5: WEATHER BY COORDINATES")
    print("="*70)

    print("\n📍 Enter coordinates (e.g., Lagos: 6.5244, 3.3792)")

    try:
        lat = float(input("Latitude: "))
        lon = float(input("Longitude: "))

        print(f"\n🌐 Fetching weather for coordinates ({lat}, {lon})...")

        url = f"{BASE_URL}/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            city = data.get('name', 'Unknown Location')
            temp = data['main']['temp']
            conditions = data['weather'][0]['description']
            humidity = data['main']['humidity']

            print("\n" + "="*70)
            print(f"📍 Location: {city}")
            print(f"🌡️  Temperature: {temp}°C")
            print(f"☁️  Conditions: {conditions.title()}")
            print(f"💧 Humidity: {humidity}%")
            print("="*70)

        else:
            print("❌ Invalid coordinates!")

    except ValueError:
        print("❌ Invalid coordinates! Use numbers (e.g., 6.5244)")
    except Exception as e:
        print(f"❌ Error: {e}")


# ============================================
# MAIN MENU
# ============================================

print("\n💡 TIP: Get your own FREE API key at openweathermap.org!")
print("   Using demo key for now - may be slow.")

while True:
    print("\n" + "="*70)
    print("              WEATHER DASHBOARD MENU")
    print("="*70)
    print("1. 🌡️  Current Weather (any city)")
    print("2. 📅 5-Day Forecast")
    print("3. 🌍 Compare Multiple Cities")
    print("4. ⭐ Favorites Dashboard")
    print("5. 📍 Weather by Coordinates")
    print("6. ❤️  Manage Favorites")
    print("7. 🚪 Exit")
    print("="*70)

    choice = input("\nYour choice (1-7): ")

    if choice == "1":
        get_current_weather()

    elif choice == "2":
        get_forecast()

    elif choice == "3":
        compare_cities()

    elif choice == "4":
        favorites_dashboard()

    elif choice == "5":
        weather_by_coordinates()

    elif choice == "6":
        print("\n💾 Favorite Cities:")
        if favorite_cities:
            for i, city in enumerate(favorite_cities, 1):
                print(f"   {i}. {city}")
        else:
            print("   (None yet)")

    elif choice == "7":
        print("\n" + "="*70)
        print("Thanks for using Weather Dashboard!")
        print("Stay weather-aware! 🌤️")
        print("="*70)
        break

    else:
        print("\n❌ Invalid choice! Pick 1-7")
