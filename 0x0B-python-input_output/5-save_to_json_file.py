#!/usr/bin/python3
""" Object to text file """


import json

def save_to_json_file(my_obj, filename):
    """ Save JSON file """
    
    with open(filename, mode='a', encoding="UTF-8") as file:
        save_Jason = json.dumps(my_obj)
        file.write(save_Jason)
