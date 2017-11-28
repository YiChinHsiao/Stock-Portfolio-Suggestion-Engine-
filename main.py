from flask import Flask, request, render_template
from investingstrategies import *

application = Flask(__name__)	

@application.route('/')
def suggestion():	

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
		if int(strategy[0]) == 1:
			result = EthicalInvesting(money)
		elif int(strategy[0]) == 2:
			result = GrowthInvesting(money)
		elif int(strategy[0]) == 3:
			result = IndexInvesting(money)
		elif int(strategy[0]) == 4:
			result = QualityInvesting(money)
		else:
			result = ValueInvesting(money)
		return render_template('suggestion.html', result=result)
	# input number of strategy is 2
	else:
		result = dict()
		for i in range(0, len(strategy)):
			if int(strategy[i]) == 1:
				result.setdefault('strategies', []).append(EthicalInvesting(money / 2.0))
			elif int(strategy[i]) == 2:
				result.setdefault('strategies', []).append(GrowthInvesting(money / 2.0))
			elif int(strategy[i]) == 3:
				result.setdefault('strategies', []).append(IndexInvesting(money / 2.0))
			elif int(strategy[i]) == 4:
				result.setdefault('strategies', []).append(QualityInvesting(money / 2.0))
			else:
				result.setdefault('strategies', []).append(ValueInvesting(money / 2.0))
		return render_template('suggestion.html', result=result)

if __name__ == '__main__':
    application.run(host='0.0.0.0',debug = True)