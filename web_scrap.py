import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"

print("Sending request...")
response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    print("Quotes found:", len(quotes))

    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        print(f"{text} - {author}")
else:
    print("Failed to retrieve page")
