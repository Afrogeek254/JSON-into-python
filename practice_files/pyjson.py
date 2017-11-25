#loading a json string into a python object 

'''Javascript Object Notation '''


import json


#json  objects are parsed as dicts in python 
people_string = '''
{
    "people": [
        {
            "name": "Danson Mwema",
            "phone" : "+254716547840",
            "emails": ["mwemadanson@outlook.com","dannymwema@gmail.com"],
            "has_license":false 

        },
        {
            "name": "Slay Queen ",
            "phone" : "+254700111111",
            "emails": null,
            "has_license":true 




        }

    ]

}
'''

data = json.loads(people_string)

for person in data['people']:
    print (person['name'])
