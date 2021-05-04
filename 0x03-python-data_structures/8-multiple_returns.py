#!/usr/bin/python3
def multiple_returns(sentence):
    lenth = len(sentence)
    if lenth > 0:
        f_word = sentence[0]
        new_tuple = [lenth, f_word]
        return(new_tuple)
    else:
        return(lenth, None)
