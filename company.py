import requests
import datetime
from googlefinance.client import get_price_data

def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)
    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol and (x['exchDisp'] == "NASDAQ" or "NYSE"):
            return x['exchDisp']+"$$$$$"+x['name']

while True:
    try:
        inputSymbol = (input("Please enter a symbol: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        try:
            returnValue = get_symbol(inputSymbol)
        except:
            print("Sorry, seems no internet or API down")
            continue
        if returnValue is None:
            print("Your Symbol is not existing in Nasdaq, please try again, like AAPL")
            continue
        else:
            results = returnValue.split("$$$$$")
            company = results[1]
            stockMarket = results[0]
            param = {
                'q': inputSymbol,  # Stock symbol (ex: "AAPL")
                'i': "86400",  # Interval size in seconds ("86400" = 1 day intervals)
                'x': stockMarket,  # Stock exchange symbol on which stock is traded (ex: "NASD")
                'p': "3d"  # Period (Ex: "1Y" = 1 year)
            }
            # get price data (return pandas dataframe)
            df = get_price_data(param)
            try:
                df.values[2]
                changed_dollar = df.values[2][3] - df.values[1][3]
                yest_close = df.values[1][3]
                today_close = df.values[2][3]
            except IndexError:
                changed_dollar = df.values[1][3] - df.values[0][3]
                yest_close = df.values[0][3]
                today_close = df.values[1][3]

            #changed_dollar = df.values[1][3] - df.values[0][3]
            if changed_dollar >= 0:
                sign = "+"
            else:
                sign = ""
            changed_percentage = 100 * changed_dollar / yest_close

            # print(changed_dollar)
            # print("{0:.2f}%".format(changed_percentage))

            print("Output:")
            print(datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y"))
            print("Company name: " + company)
            print(str(today_close) + " " + sign + str(changed_dollar) + "(" + sign + "{0:.2f}%".format(
                changed_percentage) + ")")
            continue
        break
