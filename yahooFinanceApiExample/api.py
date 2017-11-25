#case study of the yahoo finance / currency api that converts the us currency into other currencies 

import json


from urllib.request import urlopen

#pull down  this data from json file convert the data into a python object then parse out some info from it
with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

#to print the api 
#print(source)
 

data = json.loads(source) #note we`ve used the loads since its a string

#printing it out the python objects in nice format(indent= 2)
#print(json.dumps(data, indent= 2 ))


#testing to see if we have 188 resources as per our data (output shd be 188 as per count)
#print(len(data['list']['resources'])) 

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    print(name, price)



    