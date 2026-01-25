# Day 26 - Web Scraping Basics

import requests
from bs4 import BeautifulSoup

print("="*60)
print("        WEB SCRAPING - EXAMPLE 1")
print("="*60)

# Step 1: Get the webpage
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find all quotes
quotes = soup.find_all('span', class_='text')

# Step 4: Print them
print("\n📜 QUOTES:\n")
for quote in quotes:
    print(quote.text)
    print()
