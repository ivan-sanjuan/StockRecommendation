import json
from stock_utils import input_stock

with open(r'stock_directory.json', 'r') as file:
    stock_directory = json.load(file)
    
    results = []
    def scrape_and_parse(stock_code):
        input_stock = stock_code
        for stock_symbol in stock_directory:
            if stock_symbol.get('stock_symbol') == input_stock:
               cmpy_id = stock_symbol.get('cmpy_id')
               security_id = stock_symbol.get('security_id')
               company_name = stock_symbol.get('company_name')
               results.append({
                   'cmpy_id': cmpy_id,
                   'security_id': security_id,
                   'company_name': company_name
               })
        return results