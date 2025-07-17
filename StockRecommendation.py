from ph_stock_scraper import scrape_and_parse
from pse_fundamentals_scraper import search_fundamentals_data
from pse_basic_scraper import search_basic_data

raw_input_data = input('Enter Stock Symbol: ').upper()

basic_data = search_basic_data(raw_input_data)
financial_data = search_fundamentals_data(raw_input_data)
stock_directory = scrape_and_parse(raw_input_data)

class Stock():
    def __init__(self,basic_data,financial_data,stock_directory):
        self.name = stock_directory[0]['company_name']
        self.last = basic_data.get('Last Traded Price')
        self.open = basic_data.get('Open')
        self.close = basic_data.get('Previous Close and Date')
        self.high = basic_data.get('High')
        self.low = basic_data.get('Low')
        self.week_high = basic_data.get('52-Week High')
        self.week_low = basic_data.get('52-Week Low')
        self.cap = financial_data[0][1]
        self.ratio = financial_data[1][1]
        self.div = financial_data[3][1]
        self.vol = financial_data[4][1]
        self.year = financial_data[5][1]
        
    def __str__(self):
        return f'''
        Company: {self.name}
        Last Traded Price: {self.last}
        Open: {self.open}
        Close: {self.close}
        High: {self.high}
        Low: {self.low}
        52-Week High: {self.week_high}
        52-Week Low: {self.week_low}
        
        Market Capitalization: {self.cap}
        P/E Ratio: {self.ratio}
        Volatility: {self.vol}
        Divident Yield: {self.div}
        1-Year Return {self.year}
        '''

company_data = (basic_data,financial_data,stock_directory)
company = Stock(*company_data)

print(company)

