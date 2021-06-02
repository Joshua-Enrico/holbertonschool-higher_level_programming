#!/usr/bin/python3
"""
load_from_json_file function
"""


import json


def load_from_json_file(filename):
    """creates and object from a json file"""
    with open(filename, 'r', encoding="utf8") as file:
        new_obj = json.load(file)
    return new_obj
