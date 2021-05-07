#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for elm in a_dictionary.copy():
        if value == a_dictionary[elm]:
            del a_dictionary[elm]

    return a_dictionary
