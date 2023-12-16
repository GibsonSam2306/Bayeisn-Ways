import requests

api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"


def get_bitcoin_price():
    response = requests.get(api_url)
    data = response.json()
    return float(data["bpi"]["USD"]["rate"])
data_points = []

for i in range(288):
    usd_price = get_bitcoin_price()

    if not data_points or usd_price != data_points[-1]:
        data_points.append(usd_price)
    else:
        while usd_price == data_points[-1]:
            usd_price = get_bitcoin_price()

highest_price = data_points[0]
lowest_price = data_points[0]

for price in data_points:
    if price > highest_price:
        highest_price = price
    elif price < lowest_price:
        lowest_price = price

print("Highest Price (USD):", highest_price)
print("Lowest Price (USD):", lowest_price)
