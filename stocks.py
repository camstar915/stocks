from yahoo_fin import stock_info as si

# Set dictionary of how many shares I owned of each stock
portfolio = {
    "shop": 13,
    "tsla": 11,
    "googl": 1,
    "f": 108,
    "dis": 5,
    "twtr": 10,
    "pypl": 3,
    "bzun": 5,
    "ttwo": 2
}

soldAt = '16833.78'

# Function to get live stock price
def price(stock):
    return si.get_live_price(stock)

def portfolioEquity():
    total = 0
    for stock in portfolio:
        equity = price(stock) * portfolio.get(stock)
        total += equity
    return str(total)

# inclTSLA = input("With or without Tesla? : ").lower()
print('Including TSLA:')
print('Sold at: ' + soldAt)
print('Current Value: ' + portfolioEquity())

del portfolio["tsla"]
soldAt = str(round(float(soldAt) - 6437.25, 2))
print('Not including TSLA:')
print('Sold at: ' + soldAt)
print('Current Value: ' + portfolioEquity())
