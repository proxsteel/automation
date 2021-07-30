#!/usr/bin/env python3

import json
import yaml

#example_data is a dictionary of objects and nested list and dictionary    
example_data = {
    'a_list': [1,2,3,4,5],                   #is a key with a value == a list
    'a_string': 'Some Text 123',             # value == a string    
    'a_bool': True,                          # value == a bool
    'a_dict': {'val_1': 11, 'val_2': 22},     # value == a dictionary
    'a_numb': 555                             # value == a number  
}

print("Here is JSON encoding: \n")
#print(json.dumps(example_data))
print(json.dumps(example_data, indent=2))
print("-" * 100)

print("Here is YAML encoding: \n")
print(yaml.dump(example_data, default_flow_style=False))  #default is False and can be ommitet in python3
print("*" * 100)
print(yaml.dump(example_data, default_flow_style=True))
