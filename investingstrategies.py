#Investing Strategies API
from retrievestockinfo import *

def EthicalInvesting(money):
	ticker_symbol_list = ['AAPL', 'ADBE','GOOG']
	div_money = 1.0 * money / len(ticker_symbol_list)
	info = getStockInfoList(ticker_symbol_list)
	for i in range(len(ticker_symbol_list)):
		info['stocks'][i]['quantity'] = int(div_money / info['stocks'][i]['prices'][0])
		left_money = div_money - info['stocks'][i]['quantity'] * info['stocks'][i]['prices'][0]
		div_money += left_money
	
	return info
	
def GrowthInvesting(money):
	ticker_symbol_list = ['MSFT', 'FB','T']
	div_money = 1.0 * money / len(ticker_symbol_list)
	info = getStockInfoList(ticker_symbol_list)
	for i in range(len(ticker_symbol_list)):
		info['stocks'][i]['quantity'] = int(div_money / info['stocks'][i]['prices'][0])
		left_money = div_money - info['stocks'][i]['quantity'] * info['stocks'][i]['prices'][0]
		div_money += left_money
	
	return info
	
def IndexInvesting(money):
	ticker_symbol_list = ['INTC', 'ORCL','VZ']
	div_money = 1.0 * money / len(ticker_symbol_list)
	info = getStockInfoList(ticker_symbol_list)
	for i in range(len(ticker_symbol_list)):
		info['stocks'][i]['quantity'] = int(div_money / info['stocks'][i]['prices'][0])
		left_money = div_money - info['stocks'][i]['quantity'] * info['stocks'][i]['prices'][0]
		div_money += left_money
	
	return info
	
def QualityInvesting(money):
	ticker_symbol_list = ['CSCO', 'IBM','SAP']
	div_money = 1.0 * money / len(ticker_symbol_list)
	info = getStockInfoList(ticker_symbol_list)
	for i in range(len(ticker_symbol_list)):
		info['stocks'][i]['quantity'] = int(div_money / info['stocks'][i]['prices'][0])
		left_money = div_money - info['stocks'][i]['quantity'] * info['stocks'][i]['prices'][0]
		div_money += left_money
	
	return info
	
def ValueInvesting(money):
	ticker_symbol_list = ['BIDU', 'CRM','ATVI']
	div_money = 1.0 * money / len(ticker_symbol_list)
	info = getStockInfoList(ticker_symbol_list)
	for i in range(len(ticker_symbol_list)):
		info['stocks'][i]['quantity'] = int(div_money / info['stocks'][i]['prices'][0])
		left_money = div_money - info['stocks'][i]['quantity'] * info['stocks'][i]['prices'][0]
		div_money += left_money
	
	return info