revenue = 0
prices, amounts = [250, 100], [4, 10]

for price, amount in zip(prices, amounts):
    revenue += price * amount

print(revenue)
