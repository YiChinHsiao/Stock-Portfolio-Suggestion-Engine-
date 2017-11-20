#Investing Strategies API
from retrievestockinfo import getStockInfo
import json

def EthicalInvesting(money):
	stock_num = 3
	div_money = money / 3
	
	info1 = getStockInfo('AAPL')
	info2 = getStockInfo('ADBE')
	info3 = getStockInfo('GOOG')
	
	info1['quantity'] = int(div_money / info1['prices'][0])
	left_money = div_money - info1['quantity'] * info1['prices'][0]
	div_money += left_money
	info2['quantity'] = int(div_money / info2['prices'][0])
	left_money = div_money - info2['quantity'] * info2['prices'][0]
	div_money += left_money
	info3['quantity'] = int(div_money / info3['prices'][0])
	left_money = div_money - info3['quantity'] * info3['prices'][0]
	
	result = dict()
	result.setdefault('stocks', []).append(info1)
	result.setdefault('stocks', []).append(info2)
	result.setdefault('stocks', []).append(info3)
	
	return result
	
def GrowthInvesting(money):
	stock_num = 3
	div_money = money / 3
	
	info1 = getStockInfo('AAPL')
	info2 = getStockInfo('ADBE')
	info3 = getStockInfo('GOOG')
	
	info1['quantity'] = int(div_money / info1['prices'][0])
	left_money = div_money - info1['quantity'] * info1['prices'][0]
	div_money += left_money
	info2['quantity'] = int(div_money / info2['prices'][0])
	left_money = div_money - info2['quantity'] * info2['prices'][0]
	div_money += left_money
	info3['quantity'] = int(div_money / info3['prices'][0])
	left_money = div_money - info3['quantity'] * info3['prices'][0]
	
	result = dict()
	result.setdefault('stocks', []).append(info1)
	result.setdefault('stocks', []).append(info2)
	result.setdefault('stocks', []).append(info3)
	
	return result
	
def IndexInvesting(money):
	stock_num = 3
	div_money = money / 3
	
	info1 = getStockInfo('AAPL')
	info2 = getStockInfo('ADBE')
	info3 = getStockInfo('GOOG')
	
	info1['quantity'] = int(div_money / info1['prices'][0])
	left_money = div_money - info1['quantity'] * info1['prices'][0]
	div_money += left_money
	info2['quantity'] = int(div_money / info2['prices'][0])
	left_money = div_money - info2['quantity'] * info2['prices'][0]
	div_money += left_money
	info3['quantity'] = int(div_money / info3['prices'][0])
	left_money = div_money - info3['quantity'] * info3['prices'][0]
	
	result = dict()
	result.setdefault('stocks', []).append(info1)
	result.setdefault('stocks', []).append(info2)
	result.setdefault('stocks', []).append(info3)
	
	return result
	
def QualityInvesting(money):
	stock_num = 3
	div_money = money / 3
	
	info1 = getStockInfo('AAPL')
	info2 = getStockInfo('ADBE')
	info3 = getStockInfo('GOOG')
	
	info1['quantity'] = int(div_money / info1['prices'][0])
	left_money = div_money - info1['quantity'] * info1['prices'][0]
	div_money += left_money
	info2['quantity'] = int(div_money / info2['prices'][0])
	left_money = div_money - info2['quantity'] * info2['prices'][0]
	div_money += left_money
	info3['quantity'] = int(div_money / info3['prices'][0])
	left_money = div_money - info3['quantity'] * info3['prices'][0]
	
	result = dict()
	result.setdefault('stocks', []).append(info1)
	result.setdefault('stocks', []).append(info2)
	result.setdefault('stocks', []).append(info3)
	
	return result
	
def ValueInvesting(money):
	stock_num = 3
	div_money = money / 3
	
	info1 = getStockInfo('AAPL')
	info2 = getStockInfo('ADBE')
	info3 = getStockInfo('GOOG')
	
	info1['quantity'] = int(div_money / info1['prices'][0])
	left_money = div_money - info1['quantity'] * info1['prices'][0]
	div_money += left_money
	info2['quantity'] = int(div_money / info2['prices'][0])
	left_money = div_money - info2['quantity'] * info2['prices'][0]
	div_money += left_money
	info3['quantity'] = int(div_money / info3['prices'][0])
	left_money = div_money - info3['quantity'] * info3['prices'][0]
	
	result = dict()
	result.setdefault('stocks', []).append(info1)
	result.setdefault('stocks', []).append(info2)
	result.setdefault('stocks', []).append(info3)
	
	return result