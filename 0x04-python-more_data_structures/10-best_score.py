#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        value = 0
        for key in a_dictionary:
            if value < a_dictionary[key]:
                    value = a_dictionary[key]
                    user = key
        return user
    else:
        return None
