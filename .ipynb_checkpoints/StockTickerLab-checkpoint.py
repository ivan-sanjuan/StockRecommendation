import yfinance as yf

stock = yf.Ticker("AAPL")
stock.info["regularMarketPrice"]
stock.info["marketCap"]
stock.info["trailingPE"]
stock.history(period="1mo")
stock.recommendations["RECO"]

print("Company Name:", stock.info["longName"])
print("Current Price:", stock.info["regularMarketPrice"])
print("Market Cap:", stock.info["marketCap"])
print("PE Ratio:", stock.info["trailingPE"])
print("PE Ratio:", stock.history(period="1mo"))
print("PE Ratio:", stock.recommendations["RECO"])
