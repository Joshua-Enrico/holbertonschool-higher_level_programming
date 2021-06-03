#!/usr/bin/python3
"""
this script add all arguments to a python list and
save them into a specific given file
"""


from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    j_list = load_from_json_file(filename)

except:
    j_list = []

for arguments in argv[1:]:
    j_list.append(arguments)

save_to_json_file(j_list, filename)
