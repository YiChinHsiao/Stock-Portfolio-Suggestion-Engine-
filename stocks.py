strategystocks = [ ["AAPL", "ADBE", "NSRGY"],   #Ethical Investing
                   ["AAPL", "ADBE", "NSRGY"],   #Growth Investing 
                   ["VTI", "IXUS", "ILTB"],     #Index Investing 
                   ["AAPL", "ADBE", "NSRGY"],   #Quality Investing 
                   ["AAPL", "ADBE", "NSRGY"], ] #Value Investing 


class PortfolioStockEntry:
    def __init__(self, stockSymbol):
        self.symbol = stockSymbol
        self.stockfullname = ""
        self.strategy = 999999
        self.quantity = 0
        self.price = []
        self.date = []


    def printinfo(self):
        print "Stock Symbol: " , self.symbol
        print "Stock Full Name: " , self.stockfullname
        print "Stock in Strategy: " , self.strategy
        print "Stock Quantity: " , self.quantity
        print "Stock Price: \n" , 
        for i in range(0, len(self.price)):
          print self.date[i] , " : " , self.price[i]
