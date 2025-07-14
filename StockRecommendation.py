import importlib
import ph_scraper
import requests
import pprint
from bs4 import BeautifulSoup
from ph_scraper import scrape_and_parse

stock_info = scrape_and_parse()

if  stock_info  and len(stock_info) > 0:
    cmpy_id = stock_info[0]['cmpy_id']
    security_id = stock_info[0]['security_id']
    company_name = stock_info[0]['company_name']
    url = f'https://edge.pse.com.ph/companyPage/stockData.do?cmpy_id={cmpy_id}&security_id={security_id}'
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table', class_='view')
    stock_table = tables[1]
    stock_data = {}

    for row in stock_table.find_all('tr'):
        cells = row.find_all("td")
        labels = row.find_all('th')
        for label, cell in zip(labels, cells):
            key = label.get_text(strip=True)
            value = cell.get_text(strip=True)
            stock_data[key] = value
    #pprint.pprint(stock_data)

else:
    print('No matching stock found.')
    

class Stock():
    def __init__(self,stock_info,stock_data):
        self.name = stock_info[0]['company_name']
        self.open = stock_data.get('Open', 'N/A')
        self.close = stock_data.get('Last Traded Price', 'N/A')

    def __str__(self):
        return f'''
        Company: {self.name}
        Open: {self.open}
        Close: {self.close}
        '''

company = Stock(stock_info, stock_data)

print(company)

