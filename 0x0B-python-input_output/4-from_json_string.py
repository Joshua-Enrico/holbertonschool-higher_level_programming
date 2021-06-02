#!/usr/bin/python3
"""
to_json_string function
"""


import json


def from_json_string(my_str):
    """Returns an object from a json object string"""
    return json.loads(my_str)
