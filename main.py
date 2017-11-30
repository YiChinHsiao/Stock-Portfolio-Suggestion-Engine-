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
            result = EthicalInvesting(money)
        elif int(strategy[0]) == 2:
            result = GrowthInvesting(money)
        elif int(strategy[0]) == 3:
            result = IndexInvesting(money)
        elif int(strategy[0]) == 4:
            result = QualityInvesting(money)
        else:
            result = ValueInvesting(money)
        resp = make_response(jsonify(result))
        resp.headers['Access-Control-Allow-Origin'] = '*'
    	return resp
    # input number of strategy is 2
    else:
        temp1 = dict()
        temp2 = dict()
        result = dict()
        for i in range(0, len(strategy)):
            if int(strategy[i]) == 1:
            	if i == 0:
            		temp1 = EthicalInvesting((money / 2.0))
                else:
                	temp2 = EthicalInvesting((money / 2.0))
                	result = {key:(temp1[key], temp2[key]) for key in temp1}
            elif int(strategy[i]) == 2:
                if i == 0:
                	temp1 = GrowthInvesting((money / 2.0))
                else:
                	temp2 = GrowthInvesting((money / 2.0))
                	result = {key:(temp1[key], temp2[key]) for key in temp1}
            elif int(strategy[i]) == 3:
                if i == 0:
                	temp1 = IndexInvesting((money / 2.0))
                else:
                	temp2 = IndexInvesting((money / 2.0))
                	result = {key:(temp1[key], temp2[key]) for key in temp1}
            elif int(strategy[i]) == 4:
                if i == 0:
                	temp1 = QualityInvesting((money / 2.0))
                else:
                	temp2 = QualityInvesting((money / 2.0))
                	result = {key:(temp1[key], temp2[key]) for key in temp1}
            else:
                if i == 0:
                	temp1 = ValueInvesting((money / 2.0))
                else:
                	temp2 = ValueInvesting((money / 2.0))
                	result = {key:(temp1[key], temp2[key]) for key in temp1}
        resp = make_response(jsonify(result))
        resp.headers['Access-Control-Allow-Origin'] = '*'
    	return resp

if __name__ == '__main__':
	main()