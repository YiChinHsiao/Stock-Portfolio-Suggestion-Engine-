from flask import Flask, request, render_template, jsonify, make_response
from investingstrategies import *
from retrievestockinfo import *
import settings
import json
import os

application = Flask(__name__)

def main():
	settings.init()
	settings.info1 = getStockInfoList(['AAPL', 'ADBE', 'GOOG'])
	settings.info2 = getStockInfoList(['MSFT', 'FB', 'TSM'])
	settings.info3 = getStockInfoList(['INTC', 'ORCL', 'VZ'])
	settings.info4 = getStockInfoList(['CSCO', 'IBM', 'SAP'])
	settings.info5 = getStockInfoList(['BIDU', 'CRM', 'ATVI'])
	application.run(host='0.0.0.0', debug = True)

@application.route('/')
def suggestion():
    money = request.args.get('money')
    strategy = request.args.get('strategy')
    money = int(money)
    strategy = strategy.split(',')
    # input number of strategy is 1
    if len(strategy) == 1:
    	result = dict()
        if int(strategy[0]) == 1:
        	result.setdefault('strategies', []).append(EthicalInvesting(money))
        elif int(strategy[0]) == 2:
        	result.setdefault('strategies', []).append(GrowthInvesting(money))
        elif int(strategy[0]) == 3:
        	result.setdefault('strategies', []).append(IndexInvesting(money))
        elif int(strategy[0]) == 4:
        	result.setdefault('strategies', []).append(QualityInvesting(money))
        else:
        	result.setdefault('strategies', []).append(ValueInvesting(money))
        resp = make_response(jsonify(result))
        resp.headers['Access-Control-Allow-Origin'] = '*'
    	return resp
    # input number of strategy is 2
    else:
        temp = dict()
        result = dict()
        for i in range(0, len(strategy)):
            if int(strategy[i]) == 1:
            	if i == 0:
            		temp = EthicalInvesting((money / 2.0))
            		result.setdefault('strategies', []).append(EthicalInvesting(money))
                else:
                	temp = EthicalInvesting((money / 2.0))
                	result.setdefault('strategies', []).append(EthicalInvesting(money))
            elif int(strategy[i]) == 2:
                if i == 0:
                	temp = GrowthInvesting((money / 2.0))
                	result.setdefault('strategies', []).append(GrowthInvesting(money))
                else:
                	temp = GrowthInvesting((money / 2.0))
                	result.setdefault('strategies', []).append(GrowthInvesting(money))
            elif int(strategy[i]) == 3:
                if i == 0:
                	temp = IndexInvesting((money / 2.0))
                	result.setdefault('strategies', []).append(IndexInvesting(money))
                else:
                	temp = IndexInvesting((money / 2.0))
                	result.setdefault('strategies', []).append(IndexInvesting(money))
            elif int(strategy[i]) == 4:
                if i == 0:
                	temp = QualityInvesting((money / 2.0))
                	result.setdefault('strategies', []).append(QualityInvesting(money))
                else:
                	temp = QualityInvesting((money / 2.0))
                	result.setdefault('strategies', []).append(QualityInvesting(money))
            else:
                if i == 0:
                	temp = ValueInvesting((money / 2.0))
                	result.setdefault('strategies', []).append(ValueInvesting(money))
                else:
                	temp = ValueInvesting((money / 2.0))
                	result.setdefault('strategies', []).append(ValueInvesting(money))
        resp = make_response(jsonify(result))
        resp.headers['Access-Control-Allow-Origin'] = '*'
    	return resp

if __name__ == '__main__':
	main()