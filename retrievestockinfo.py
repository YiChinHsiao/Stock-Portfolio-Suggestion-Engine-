#!/usr/bin/env python

#Project: Stock Info Retreive API
import json
import urllib2
from yahoofinancials import YahooFinancials
from time import strftime
import datetime


def main():
    #Testing API Purpose

    ticker_symbol = "AAPL"

    price_list = []
    date_list = []

    ticker_name = getStockPrice(ticker_symbol, price_list, date_list)

    #print week_go
    #print stock_info
    print ticker_name
    for p in date_list: print p
    for p in price_list: print p

def getStockPrice(ticker_symbol, price_list, date_list):
    stock = YahooFinancials(ticker_symbol)
    stock_info = stock.get_stock_price_data()

    fullname = stock_info[ticker_symbol]['longName']

    today = datetime.datetime.today().strftime('%Y-%m-%d')
    week_ago = (datetime.datetime.today() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    stock_price = stock.get_historical_stock_data(week_ago, today, "daily")

    for i in range(len(stock_price[ticker_symbol]['prices'])):
      price_list.append(stock_price[ticker_symbol]['prices'][i]['close'])
      date_list.append(stock_price[ticker_symbol]['prices'][i]['formatted_date'])


    return fullname


if __name__ == "__main__":
    main()