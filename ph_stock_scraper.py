import json

with open(r'stock_directory.json', 'r') as file:
    stock_directory = json.load(file)
    
    results = []
    def scrape_and_parse(raw_input_data):
        input_stock = raw_input_data
        for stock in stock_directory:
            if stock.get('stock_symbol') == input_stock:
                cmpy_id = stock.get('cmpy_id')
                security_id = stock.get('security_id')
                company_name = stock.get('company_name')
                results.append({
                    'cmpy_id': cmpy_id,
                    'security_id': security_id,
                    'company_name': company_name
                })
        return results        
    
        

                
