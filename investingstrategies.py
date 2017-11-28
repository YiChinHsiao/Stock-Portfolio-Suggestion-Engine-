#Investing Strategies API
from retrievestockinfo import getStockInfo

def EthicalInvesting(money):
	stock_num = 3
	div_money = money / 3.0
	
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
	div_money = money / 3.0
	
	info1 = getStockInfo('MSFT')
	info2 = getStockInfo('FB')
	info3 = getStockInfo('T')
	
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
	div_money = money / 3.0
	
	info1 = getStockInfo('INTC')
	info2 = getStockInfo('ORCL')
	info3 = getStockInfo('VZ')
	
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
	div_money = money / 3.0
	
	info1 = getStockInfo('CSCO')
	info2 = getStockInfo('IBM')
	info3 = getStockInfo('SAP')
	
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
	div_money = money / 3.0
	
	info1 = getStockInfo('BIDU')
	info2 = getStockInfo('CRM')
	info3 = getStockInfo('ATVI')
	
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