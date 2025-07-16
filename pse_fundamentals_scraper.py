from bs4 import BeautifulSoup
import requests
import json

with open(r'stock_directory.json', 'r') as file:
    stock_directory = json.load(file)
    
def search_fundamentals_data(raw_input_data):
    url = f'https://dividends.ph/company/{raw_input_data}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find_all('tr')
    parsed_data = []
    for row in data:
        cells = row.find_all('td')
        parsed_data.append([cell.get_text(strip=True) for cell in cells])
        
    return parsed_data
