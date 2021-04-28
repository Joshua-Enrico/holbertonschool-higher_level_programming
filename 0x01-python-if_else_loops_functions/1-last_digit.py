#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lastNumber = number % 10
else:
    lastNumber = number % -10
if lastNumber == 0:
    retorna = "and is 0"
elif lastNumber > 5:
    retorna = "and is greater than 5"
else:
    retorna = "and is less than 6 and not 0"
print("Last digit of {:d} is {:d} {}".format(number, lastNumber, retorna))
