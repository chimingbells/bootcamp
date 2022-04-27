business = ['pigs', 'chickens', 'cows']
weapdict = {"sword": "Katana", "gun": "AK-47", "tank": "Sherman"}
weaptuple = weapdict.items()
value_dict = weapdict.values()

for i in business:
    print(i)

for item in weaptuple:
    print(item)

for v in value_dict:
    print(v)


prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
def discount(current_price):
    return (current_price[0], round(current_price[1] * 0.95, 2))

def make_low_price(price):
    return prices[price] < 0.4

low_price = list(filter(make_low_price, prices.keys()))
new_prices = dict(map(discount, prices.items()))
print(new_prices)
print(low_price)