from yahoo_fin import stock_info as si
import pprint

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

# Function to get live stock price
def price(stock):
    return si.get_live_price(stock)

def portfolioEquity():
    total = 0
    for stock in portfolio:
        equity = price(stock) * portfolio.get(stock)
        total += equity
    return str("%.2f" % round(float(total), 2))

soldAt = '16833.78'
current = portfolioEquity()
diff = str("%.2f" % round(float(soldAt) - float(current), 2))
dash = '-' *30

print('\n\n\n\n' + dash)
print('Including TSLA')
print(dash)
print('{:<15s}{:>15}'.format('Sold at:', soldAt))
print('{:<15s}{:>15}'.format('Current Value:', current))
print('{:<15s}{:>15}'.format('Difference:', diff))

del portfolio["tsla"]
soldAt = str(round(float(soldAt) - 6437.25, 2))
current = portfolioEquity()
diff = str("%.2f" % round(float(soldAt) - float(current), 2))
print('\n\n' + dash)
print('Not Including TSLA')
print(dash)
print('{:<15s}{:>15}'.format('Sold at:', soldAt))
print('{:<15s}{:>15}'.format('Current Value:', current))
print('{:<15s}{:>15}'.format('Difference:', diff))
