#!/usr/bin/python3
"""
read_file functions
"""


def read_file(filename=""):
    """read a text file(utf9) and prints it"""
    with open(filename, "r", encoding=("utf8")) as text:
        lines = text.read()
    print(lines, end='')
