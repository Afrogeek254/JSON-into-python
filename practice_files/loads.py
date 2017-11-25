#loading Json files into python objects and then writing those objects writing those objects back to json files US states.json
''' Javascript object notation'''

import json

#we use the json load method to load a file into a python object and loads() loads a string

#first openthe file 

with open('states.json') as f:
    data = json.load(f)

#loop through the list of objects (states are keys )
#for state in data['states']:
    #printing the states 
    # print(state)

    #printing out the states i.e just the name and abbreviations 
    #print(state['name'], state['abbreviation'])

#writing the python object out to a json file (remove one of the keys from the data then write that to a new file )

for state in data['states']:
    del state['area_codes']
    
 # dumping this data into a json file we use json.dump() / into ajson string we use json.dumps 

with open('new_states.json', 'w') as f: # this creates a new Json file in the same folder/dir
    json.dump(data,f, indent=2)



