#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    new_list = set(my_list)
    for elm in new_list:
        add += elm
    return(add)
