import json
import urllib
from pprint import pprint

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
pprint(quote)
