from bs4 import BeautifulSoup
import requests
import json

with open(r'stock_directory.json', 'r') as file:
    stock_directory = json.load(file)

def parse_fundamentals(fundamentals):
    if fundamentals in stock_directory:
        fundamentals = fundamentals.strip().upper()
        cmpy_data = stock_directory[fundamentals]
        cmpy_id = cmpy_data.get('cmpy_id')
        if not cmpy_id:
            return {}

        url = f'https://edge.pse.com.ph/companyPage/financial_reports_view.do?cmpy_id={cmpy_id}'
        response = requests.get(url)
        html_response = response.text
        soup = BeautifulSoup(html_response,'html.parser')
        
        if not financial_data or len(financial_data) == 0:
            data_rows = soup.find_all("tr")
            
        financial_data = {}
        for row in data_rows:
            cells = row.find_all("td")
            if len(cells) == 2:
                label = cells[0].get_text(strip=True)
                value = cells[1].get_text(strip=True)
                financial_data[label] = value

        return financial_data
    




