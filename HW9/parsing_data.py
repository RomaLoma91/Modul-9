import requests
from bs4 import BeautifulSoup
import json

# Отримання HTML-коду зі сторінки
url = 'http://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Збереження цитат і авторів у списки
quotes = []
authors = []

for quote in soup.find_all('div', class_='quote'):
    text = quote.find('span', class_='text').text
    author_elem = quote.find('small', class_='author')
    
    if author_elem:
        author_name = author_elem.text
        author_url = author_elem.find_next_sibling('a')['href']
        
        quotes.append({
            'quote': text,
            'author': author_name
        })
        
        authors.append({
            'fullname': author_name,
            'born_date': '',
            'born_location': '',
            'description': '',
            'url': author_url
        })

# Збереження даних у файли
with open('quotes.json', 'w') as quotes_file:
    json.dump(quotes, quotes_file, indent=4)

with open('authors.json', 'w') as authors_file:
    json.dump(authors, authors_file, indent=4)
