#!/usr/bin/python3
"""
write_file function
"""


def write_file(filename="", text=""):
    """Write into file , create if it doesn't exit"""
    with open(filename, 'w', encoding=("utf8")) as file:
        num_c = file.write(text)
        return num_c
