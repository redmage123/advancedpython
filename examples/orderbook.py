#!/usr/bin/python3


import urllib2
from collections import namedtuple


class menuChoices(object):
     (LOGIN,REGISTER,BUY,SELL,LIST) = range(0,5)


class order (object):
    def __init__(self)
        self.orderRecord = namedtuple('orderRec','symbol','name','ask','bid')
        self.connection = connection()

    def getData(self,symbol):
        self.orderRecord = connection.send(symbol)
        return(self.orderRecord)
    
class orderBook(object):
    def __init__(self,initialBalance=100000.00):
        self.balance = initialBalance
        self.orderList = []

    def addOrder(self,orderRec):
        self.orderList.append(orderRec)

    def sellOrder(self,orderRec):
        self.orderList.append(orderRec)

class connection(object):
    def __init__(self):

        self.url = "http://finance.yahoo.com/d/quotes.csv?format=json")

    def send(self,symbol):
       response = urllib2.urlopen('http://finance.yahoo.com/d/quotes.csv?format=json&s=AAPL&f=nab')
       return(response[0])


    

    
