#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At Holberton school, I learnt C!"
sentence1 = 'ddddd   d'
length, first = multiple_returns(sentence1)
print("Length: {:d} - First character: {}".format(length, first))
