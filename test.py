from flask import Flask, request

application = Flask(__name__)

@application.route('/')
def test():
	
	money = request.args.get('money')
	return money

if __name__ == '__main__':
    application.run(host='0.0.0.0',debug = True)

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