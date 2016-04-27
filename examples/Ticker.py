#!/usr/bin/python


import urllib

class Ticker(object):
    def __init__(self):
        pass

    def consumer(self):
       while True:
            symbol = (yield)
            print ("symbol = " + symbol)
            urlstring = 'http://finance.yahoo.com/d/quotes.csv?format=json&s=\"%s\"&f=nab' % (symbol)
            response = urllib.urlopen(urlstring)
            for line in response: 
                print line

    def producer(self):
        c = self.consumer()
        c.send(None)
        c.send("GOOG")


t = Ticker()
t.producer()
print "Foobar"
