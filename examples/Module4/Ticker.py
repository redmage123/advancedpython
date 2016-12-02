#!/usr/bin/python


import urllib

class Ticker(object):
    def __init__(self):
        pass

    def consumer(self):
        symbol = (yield)
        print ("symbol = " + symbol)
        urlstring = 'http://finance.yahoo.com/d/quotes.csv?format=json&s=\"%s\"&f=nab' % (symbol)
        response = urllib.urlopen(urlstring)
        for line in response: 
            print line

    def producer(self,symbol):
        c = self.consumer()
        c.send(None)
        try:
            c.send(symbol)
        except StopIteration:
            return


t = Ticker()
t.producer('GOOG')
t.producer('AAPL')
