#dumping a python object into a json string 
'''Javascript Object Notation '''


import json 

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
    del person['phone']
#dumping the data into a json string 
new_string = json.dumps(data, indent=2, sort_keys=True) # the number of indentations per item in the json string the indent fn outputs the data well with a good indentation proper fomating in a way its easy to read

print(new_string)