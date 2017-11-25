import json 

from urllib.request import urlopen 

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()


data = json.loads(source)

#creating a new  python dict that stores the name and convresion rates 

usd_rates  = dict() #a new instance of class dict 

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price 

print(usd_rates['USD/EUR'])  # say I want to print usd/EUR rate = 0.837800(output)

#say we want to convert 100 usd to indian rupee to usd 
print(100 * float(usd_rates['USD/INR']))  # 6466.8999



