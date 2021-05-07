#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        num = 0
        div = 0
        for tupl in my_list:
            num += (tupl[0] * tupl[1])
            div += tupl[1]
        return num / div
    else:
        return 0
