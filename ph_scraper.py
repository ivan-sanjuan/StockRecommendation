import json

def scrape_and_parse():
    
    with open(r'C:\Projects\StockRecommendation\stock_directory.json', 'r') as file:
        stock_directory = json.load(file)

    symbol = input('Stock Symbol: ').upper()
    result = []
    for stock_entry in stock_directory:
        if stock_entry.get('Symbol') == symbol:
            cmpy_id = stock_entry.get('cmpy_id')
            security_id = stock_entry.get('security_id')
            result.append({
            'cmpy_id': cmpy_id,
            'security_id': security_id
            })
            break
    return result