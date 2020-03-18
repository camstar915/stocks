from yahoo_fin import stock_info as si
# import pprint

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

currentPrice = {}

soldAt = {
    'shop': 476.85,
    'tsla': 585.20,
    'googl': 1460.58,
    'f': 8.88,
    'dis': 136.04,
    'twtr': 33.78,
    'pypl': 117.05,
    'bzun': 31.62,
    'ttwo': 125.23,
    'total': 16833.78,
}

def price(stock):
    return si.get_live_price(stock)

totalCurrent = 0
grandTotalCurrent = 0
for stock in portfolio:
    value = "%.2f" % round(price(stock), 2)
    currentPrice[stock] = value
    totalCurrent += (float(value) * portfolio.get(stock))
    grandTotalCurrent += (float(value) * portfolio.get(stock))

dash = '-' * 110

print('\n\n\n\n' + dash)
print('Portfolio Summary')
print(dash)
print('{:<10s}{:>15}{:>15}{:>15}{:>10}{:>15}{:>15}{:>15}'.format('Company', 'Current Price', 'Sold At', 'Difference', 'Shares', 'Current Price', 'Sold At', 'Difference'))
for key in currentPrice:
    print('{:<10s}{:>15}{:>15}{:>15}{:>10}{:>15}{:>15}{:>15}'.format(key, currentPrice.get(key), "%.2f" % soldAt.get(key), "%.2f" % round(soldAt.get(key)-float(currentPrice.get(key)), 2), str(portfolio.get(key)) + 'x', "%.2f" % round(float(currentPrice.get(key)) * portfolio.get(key), 2), "%.2f" % round(float(soldAt.get(key)) * portfolio.get(key), 2), "%.2f" % round((float(soldAt.get(key))*portfolio.get(key))-float((float(currentPrice.get(key)) * portfolio.get(key))), 2)))
print(dash)
print('{:<10s}{:>100}'.format('Total', "%.2f" % round(soldAt['total'] - totalCurrent, 2)))
