#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    letter = {'I': 1, 'V': 5, 'X': 10,
              'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    maxchar = 'I'
    new_list = roman_string[::-1]
    for elm2 in new_list:
        if letter[elm2] >= letter[maxchar]:
            maxchar = elm2
            total += letter[elm2]
        else:
            total -= letter[elm2]
    return total
