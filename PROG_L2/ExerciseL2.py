prices = [ 120.00, 160.00, 80.00 ]

prices.append(160.00)

print(prices.count(160.00))

print(min(prices))

print(prices.index(min(prices)))

prices.remove(min(prices))

prices.sort()
print(prices)