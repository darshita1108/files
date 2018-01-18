stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YAHOO': 39.28,
    'APPLE': 99.76,
}
#a list of keys and values

print(min(zip(stocks.values(),stocks.keys())))
print(max(zip(stocks.values(),stocks.keys())))

print(sorted(zip(stocks.values(),stocks.keys())))

print(min(zip(stocks.keys(),stocks.values())))
print(max(zip(stocks.keys(),stocks.values())))

