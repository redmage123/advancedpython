#!/usr/bin/python3


import urllib2


class app(object):
    def __init__(self):
        self.ob = orderBook()

class orderBook(object):
    def __init__(self):
        self.orderDict = {}

class connection(object):
    def __init__(self):
        self.url = https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22BHP.AX%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=

        self.url = "http://finance.yahoo.com/d/quotes.csv?format=json")

response = urllib2.urlopen('http://finance.yahoo.com/d/quotes.csv?format=json&s=AAPL&f=nab')
for line in response:
    print line


    

    
