#!/usr/bin/python3

import json

def save_to_json_file(my_obj, filename):
'''writes object in a file using JSON representation'''

    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_0bj, file)
