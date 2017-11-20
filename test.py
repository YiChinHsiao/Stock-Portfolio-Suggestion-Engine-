from flask import Flask, request
from investingstrategies import *

application = Flask(__name__)	

#return json string (if 2 strategies: combine 2 json strings and then return)	
@application.route('/')
def test():	

	money = request.args.get('money')
	strategy = request.args.get('strategy')
	
	#return error if money is not given
	if not money:
		return 'The amount of money must be given'
		
	#return error if strategy is not chosen	
	if not strategy:
		return 'Must choose at least 1 strategy'
		
	strategy = strategy.split(',')
	
	#return error if more than 2 strategies are chosen
	if len(strategy) > 2:
		return 'Cannot choose more than 2 strategies'
		
	try:
		money = int(money)
		#return error if input money is less than 5000
		if money < 5000:
			return 'Money has to be at least 5000'
			
	#return error if input money is not an integer
	except ValueError:
		return 'Input (money) is not an integer'
	
	# input number of strategy is 1
	if len(strategy) == 1:
		if strategy == '1':
			result = EthicalInvesting(money)
		elif strategy == '2':
			result = GrowthInvesting(money)
		elif strategy == '3':
			result = IndexInvesting(money)
		elif strategy == '4':
			result = QualityInvesting(money)
		else:
			result = ValueInvesting(money)
		return json.dumps(result)
	# input number of strategy is 2
	else:
		return 'try later'		

if __name__ == '__main__':
    application.run(host='0.0.0.0',debug = True)

# input  1. money   2. strategy (http://0.0.0.0:5000/?money=3000&strategy=1,2)

# return each stock information (JSON)
# stock name, company name, 5 days end price, 5 days date, quantity, (left money?)