from flask import Flask, request
from retrievestockinfo import getStockPrice
from stocks import *

application = Flask(__name__)

@application.route('/')

#Stocks defined in stocks.py


def test():	

	money = request.args.get('money')
	if not money:
		return 'The amount of money must be given'
		
	strategy = request.args.get('strategy')
	if not strategy:
		return 'Must choose at least 1 strategy'
		
	strategy = strategy.split(',')
	if len(strategy) > 2:
		return 'Cannot choose more than 2 strategies'
		
	try:
		money = int(money)
		if money >= 5000:
			#return str(money)
			print strategy
			portfolio_info = []
			remainmon = SuggestinEngine(money, strategy, portfolio_info)
			return str(remainmon)

		else:
			return 'Money has to be at least 5000'
	except ValueError:
		return 'Input (money) is not an integer'

def test2():	
	money = 6000
	strategy = [1,2]

	portfolio_info = []
	remainmon = SuggestinEngine(money, strategy, portfolio_info)
	print remainmon

	for Entry in portfolio_info:
		Entry.printinfo()

	return


def SuggestinEngine(money, strategy, portfolio_info):

	money_per_stgy = money / len(strategy)
	print money_per_stgy

	for stgy in strategy:

		print stgy;
		remain_money = RunStrategy(money_per_stgy, int(stgy), portfolio_info)
		money_per_stgy = (money / len(strategy)) + remain_money

	return remain_money

def RunStrategy(money, strategy, portfolio_info):

	money_per_stock = money / len(strategystocks[strategy])

	for stock in strategystocks[strategy]:

		portfolio_entry = PortfolioStockEntry(stock)
		print stock
		portfolio_entry.stockfullname = getStockPrice(stock, portfolio_entry.price, portfolio_entry.date)

		print money_per_stock
		portfolio_entry.quantity = int(money_per_stock / portfolio_entry.price[-1])

		print portfolio_entry.price[-1]
		print portfolio_entry.quantity

		remain_cash = money_per_stock  - (portfolio_entry.price[-1] * portfolio_entry.quantity)
		money_per_stock = (money / len(strategystocks[strategy])) + remain_cash

		portfolio_entry.strategy = strategy

		#Append the entry into a list
		portfolio_info.append(portfolio_entry)

	return remain_cash


if __name__ == '__main__':
    application.run(host='0.0.0.0',debug = True)
    #test2()

# input  1. money   2. strategy (http://0.0.0.0:5000/?money=3000&strategy=1,2)

# return error
# money is not integer, money < 5000
# strategy size > 2

# return for each stock (JSON)
# stock name, company name, 5 days end price, 5 days date, quantity, left money

#API
#1. getCompanyName()
#2. get5DaysDateAndEndPrice()
#3. runS1()
#4. runS2()
#5. runS3()
#6. runS4()
#7. runS5()