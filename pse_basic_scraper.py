from bs4 import BeautifulSoup
import json
import requests

with open(r'stock_directory.json', 'r') as file:
    stock_directory = json.load(file)

def search_basic_data(raw_input_data):
    for symbol in stock_directory:
        if raw_input_data == symbol.get('stock_symbol'):
            cmpy_id = symbol.get('cmpy_id')
            security_id = symbol.get('security_id')
            url = f'https://edge.pse.com.ph/companyPage/stockData.do?cmpy_id={cmpy_id}&security_id={security_id}'
            response = requests.get(url)
            html_data = response.text
            soup = BeautifulSoup(html_data, 'html.parser')
            tables = soup.find_all('table', class_='view')
            stock_table = tables[1]
            parsed_data = {}
            for row in stock_table.find_all('tr'):
                cells = row.find_all("td")
                labels = row.find_all('th')
                for label, cell in zip(labels, cells):
                    key = label.get_text(strip=True)
                    value = cell.get_text(strip=True)
                    parsed_data[key] = value
             
    return parsed_data
