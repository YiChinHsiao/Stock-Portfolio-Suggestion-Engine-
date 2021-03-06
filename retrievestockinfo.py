#Stock Info Retreive API
from yahoofinancials import YahooFinancials
from time import strftime
import datetime
import settings

#one time get one stock information
#def getStockInfo(ticker_symbol):
#	stock = YahooFinancials(ticker_symbol)
#	stock_info = stock.get_stock_price_data()
#	return_info = dict()
#		
#	fullname = stock_info[ticker_symbol]['longName']
#	return_info['symbol'] = ticker_symbol
#	return_info['company'] = fullname
#	return_info['quantity'] = 0
#		
#	weeks_ago = (datetime.datetime.today() - datetime.timedelta(days=14)).strftime('%Y-%m-%d')
#	tomorrow = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
#	stock_price = stock.get_historical_stock_data(weeks_ago, tomorrow, "daily")
#	
#	for i in range(5):
#		return_info.setdefault('dates', []).append(stock_price[ticker_symbol]['prices'][i]['formatted_date'])
#		return_info.setdefault('prices', []).append(stock_price[ticker_symbol]['prices'][i]['close'])
#		
#	return return_info

#one time get multiple stock information
def getStockInfoList(ticker_symbol_list):
	stock = YahooFinancials(ticker_symbol_list)
	stock_info = stock.get_stock_price_data()
	return_info = dict()
	result = dict()
	
	weeks_ago = (datetime.datetime.today() - datetime.timedelta(days=14)).strftime('%Y-%m-%d')
	tomorrow = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
	stock_price = stock.get_historical_stock_data(weeks_ago, tomorrow, "daily")
	
	for i in range(len(ticker_symbol_list)):
		fullname = stock_info[ticker_symbol_list[i]]['longName']
		return_info['symbol'] = ticker_symbol_list[i]
		return_info['company'] = fullname
		return_info['quantity'] = 0
		for j in range(5):
			return_info.setdefault('dates', []).append(stock_price[ticker_symbol_list[i]]['prices'][j]['formatted_date'])
			return_info.setdefault('prices', []).append(stock_price[ticker_symbol_list[i]]['prices'][j]['close'])
		result.setdefault('stocks', []).append(return_info)
		return_info = {}
	
	return result