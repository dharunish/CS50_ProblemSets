import requests
import json
import sys


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    d = response.json()
    currency = d["bpi"]
    usd = currency["USD"]
    rate = usd["rate"]
    if len(sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit(1)
    elif isfloat(sys.argv[1]):
        amount = float(sys.argv[1])
        rate = rate.replace(",", "")
        rate = float(rate)
        print(f"${amount*rate:,.4f}")
    else:
        print("Command-line argument is not a number")
        sys.exit(1)
except requests.RequestException:
    print("Cannot access coin base")