#!/usr/bin/env python

#### 
# For windows, use this rather than /usr/bin/env python
#!c:\Python27\python.exe -u
####


import urllib2

# Gives back a CSV output
response = urllib2.urlopen('http://finance.yahoo.com/d/quotes.csv?format=json&s=AAPL&f=nab')

for line in response:
    print line

# Gives back a JSON response
response = urllib2.urlopen('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22BHP.AX%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=')

for line in response:
    print line


