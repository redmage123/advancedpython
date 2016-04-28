#!/usr/bin/python3
import urllib
import json

result urllib.urlopen('https://query.yahooapis.com/v1/public/yql?q=select wind from weather.forecast where woeid in (select woeid from geo.places(1) where text\%3D\%22chicago\%2C\%20il\%22)&format=json&env=store\%3A\%2F\%2Fdatatables.org\%2Falltableswithkeys')

jresult = json.loads(result)
print (jresult)

