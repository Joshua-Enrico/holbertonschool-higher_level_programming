#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    letter = {'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    new_list = list(roman_string)
    for elm in new_list:
        for elm2 in letter:
            if elm == elm2:
                if total < letter[elm2]:
                    total = letter[elm2] - total
                else:
                    total += letter[elm2]
                break
    return total