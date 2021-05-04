#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = my_list
    if 0 <= idx < len(my_list):
        del new_list[idx]
        return(new_list)
    else:
        return(my_list)
