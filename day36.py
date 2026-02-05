# Day 36 - Multi Crypto Collector (Step 1)

COINS = {
    "bitcoin": "BTC",
    "ethereum": "ETH",
    "binancecoin": "BNB",
    "solana": "SOL",
    "ripple": "XRP",
    "cardano": "ADA",
    "dogecoin": "DOGE",
    "tron": "TRX",
    "polkadot": "DOT",
    "litecoin": "LTC"
}

print("Tracking these coins:\n")

for coin_id, symbol in COINS.items():
    print(f"{symbol} → {coin_id}")


import requests

# Build coin ID list for API
coin_ids = ",".join(COINS.keys())

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": coin_ids,
    "vs_currencies": "usd"
}

response = requests.get(url, params=params)
data = response.json()

print("\nLive Prices:\n")

for coin_id, symbol in COINS.items():
    price = data[coin_id]["usd"]
    print(f"{symbol}: ${price}")

import pandas as pd
from datetime import datetime
import os

# Prepare rows
rows = []
timestamp = datetime.now()

for coin_id, symbol in COINS.items():
    price = data[coin_id]["usd"]

    rows.append({
        "timestamp": timestamp,
        "coin": symbol,
        "price_usd": price
    })

# Create DataFrame
df = pd.DataFrame(rows)

# File name
file_name = "crypto_prices.csv"

# Save to CSV (append if exists)
if os.path.exists(file_name):
    df.to_csv(file_name, mode="a", header=False, index=False)
else:
    df.to_csv(file_name, index=False)

print("\nData saved to crypto_prices.csv")
