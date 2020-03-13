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

# Function to get live stock price
def price(stock):
    return si.get_live_price(stock)

totalCurrent = 0
for stock in portfolio:
    value = "%.2f" % round(price(stock), 2)
    currentPrice[stock] = value
    totalCurrent += (float(value) * portfolio.get(stock))

# diff = str("%.2f" % round(float(soldAt) - float(current), 2))
dash = '-' * 55
dash2 = '-' * 45
dashTotal = '-' * 110

print('\n\n\n\n' + dash)
print('Portfolio Summary')
print(dash)
print('{:<10s}{:>15}{:>15}{:>15}{:>10}{:>15}{:>15}{:>15}'.format('Company', 'Current Price', 'Sold At', 'Difference', 'Shares', 'Current Price', 'Sold At', 'Difference'))
for key in currentPrice:
    print('{:<10s}{:>15}{:>15}{:>15}{:>10}{:>15}{:>15}{:>15}'.format(key, currentPrice.get(key), "%.2f" % soldAt.get(key), "%.2f" % round(soldAt.get(key)-float(currentPrice.get(key)), 2), str(portfolio.get(key)) + 'x', "%.2f" % round(float(currentPrice.get(key)) * portfolio.get(key), 2), "%.2f" % round(float(soldAt.get(key)) * portfolio.get(key), 2), "%.2f" % round((float(soldAt.get(key))*portfolio.get(key))-float((float(currentPrice.get(key)) * portfolio.get(key))), 2)))
print(dashTotal)
print('{:<10s}{:>100}'.format('Total', soldAt['total'] - totalCurrent))




# def portfolioEquity():
#     total = 0
#     for stock in portfolio:
#         equity = price(stock) * portfolio.get(stock)
#         total += equity
#     return str("%.2f" % round(float(total), 2))

# soldAt = '16833.78'
# current = portfolioEquity()
# diff = str("%.2f" % round(float(soldAt) - float(current), 2))
# dash = '-' *30

# print('\n\n\n\n' + dash)
# print('Including TSLA')
# print(dash)
# print('{:<15s}{:>15}'.format('Sold at:', soldAt))
# print('{:<15s}{:>15}'.format('Current Value:', current))
# print('{:<15s}{:>15}'.format('Difference:', diff))

# del portfolio["tsla"]
# soldAt = str(round(float(soldAt) - 6437.25, 2))
# current = portfolioEquity()
# diff = str("%.2f" % round(float(soldAt) - float(current), 2))
# print('\n\n' + dash)
# print('Not Including TSLA')
# print(dash)
# print('{:<15s}{:>15}'.format('Sold at:', soldAt))
# print('{:<15s}{:>15}'.format('Current Value:', current))
# print('{:<15s}{:>15}'.format('Difference:', diff))
