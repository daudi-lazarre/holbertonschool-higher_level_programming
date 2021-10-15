#!/usr/bin/python3
""" creates an Object from a “JSON file”: """


import json

def load_from_json_file(filename):
    """ From Jason to object FILE """
    
    with open(filename) as file:
        j_to_obj = json.load(file)
        return(j_to_obj)
