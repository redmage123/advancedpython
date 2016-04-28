#!/usr/bin/python

import urllib


def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.next()
        return cr
    return start

class Ticker:
    def __init__(self):
        self.c = self.consumer()
        self.p = self.producer()


    @coroutine
    def consumer(self):
        while True:
            symbol = (yield)
            urlstring = 'http://finance.yahoo.com/d/quotes.csv?format=json&s=\"%s\"&f=nab' % (symbol)
            response = urllib.urlopen(urlstring)
            for line in response: 
                print (line)

    def producer(self):
        f = open('symbols.dat','r')
#        self.c.send(None)
        for s in f:
            self.c.send(s.strip())
            yield




t = Ticker()
t.p.next()
while True:
    try:
        t.p.next()
    except StopIteration:
        break
