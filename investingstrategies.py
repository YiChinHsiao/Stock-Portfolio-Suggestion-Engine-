#Investing Strategies API
import settings 

def EthicalInvesting(money):
	div_money = money / 3.0
	result = dict()
	for i in range(3):
		settings.info1['stocks'][i]['quantity'] = int(div_money / settings.info1['stocks'][i]['prices'][0])
		left_money = div_money - settings.info1['stocks'][i]['quantity'] * settings.info1['stocks'][i]['prices'][0]
		div_money += left_money
	result = settings.info1
	
	return result
	
def GrowthInvesting(money):
	div_money = money / 3.0
	result = dict()
	for i in range(3):
		settings.info2['stocks'][i]['quantity'] = int(div_money / settings.info2['stocks'][i]['prices'][0])
		left_money = div_money - settings.info2['stocks'][i]['quantity'] * settings.info2['stocks'][i]['prices'][0]
		div_money += left_money
	result = settings.info2
	
	return result
	
def IndexInvesting(money):
	div_money = money / 3.0
	result = dict()
	for i in range(3):
		settings.info3['stocks'][i]['quantity'] = int(div_money / settings.info3['stocks'][i]['prices'][0])
		left_money = div_money - settings.info3['stocks'][i]['quantity'] * settings.info3['stocks'][i]['prices'][0]
		div_money += left_money
	result = settings.info3
	
	return result
	
def QualityInvesting(money):
	div_money = money / 3.0
	result = dict()
	for i in range(3):
		settings.info4['stocks'][i]['quantity'] = int(div_money / settings.info4['stocks'][i]['prices'][0])
		left_money = div_money - settings.info4['stocks'][i]['quantity'] * settings.info4['stocks'][i]['prices'][0]
		div_money += left_money
	result = settings.info4
	
	return result
	
def ValueInvesting(money):
	div_money = money / 3.0
	result = dict()
	for i in range(3):
		settings.info5['stocks'][i]['quantity'] = int(div_money / settings.info5['stocks'][i]['prices'][0])
		left_money = div_money - settings.info5['stocks'][i]['quantity'] * settings.info5['stocks'][i]['prices'][0]
		div_money += left_money
	result = settings.info5
	
	return result