#Stock Info Retreive API
from yahoofinancials import YahooFinancials
from time import strftime
import datetime

def getStockInfo(ticker_symbol):
	stock = YahooFinancials(ticker_symbol)
	stock_info = stock.get_stock_price_data()
	return_info = dict()
		
	fullname = stock_info[ticker_symbol]['longName']
	return_info['symbol'] = ticker_symbol
	return_info['company'] = fullname
	return_info['quantity'] = 0
		
	week_ago = (datetime.datetime.today() - datetime.timedelta(days=6)).strftime('%Y-%m-%d')
	tomorrow = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
	stock_price = stock.get_historical_stock_data(week_ago, tomorrow, "daily")
	
	for i in range(len(stock_price[ticker_symbol]['prices'])):
		return_info.setdefault('dates', []).append(stock_price[ticker_symbol]['prices'][i]['formatted_date'])
		return_info.setdefault('prices', []).append(stock_price[ticker_symbol]['prices'][i]['close'])
		
	return return_info