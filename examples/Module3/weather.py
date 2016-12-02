#!/usr/bin/env python
import json
import urllib
from pprint import pprint

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
             pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


# Example usage
class weatherData(Subject):
    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self.data = 0

    def setData(self, data):


        base_url = 'https://query.yahooapis.com/v1/public/yql?'
        query = {
            'q': 'select * from yahoo.finance.quote where symbol in ("YHOO","AAPL")',
            'format': 'json',
            'env': 'store://datatables.org/alltableswithkeys'
        }

        url = base_url + urllib.urlencode(query)
        response = urllib.urlopen(url)
        data = response.read()
        quote = json.loads(data)
        self.data = quote
        self.notify()

    def getData(self):
        return self.data


class WeatherViewer(object):
    def update(self, subject):
        print 'Weather is: %s' % (subject.getData())



# Example usage...
def main():
   w1 = WeatherViewer()
   d1 = weatherData('Dublin')
   d2 = weatherData('Riga')
   d3 = weatherData('London')
   d4 = weatherData('Dublin')
   d1.attach(w1)
   d1.attach(d2)
   while True:
       pass
if __name__ == '__main__':
    main() 
