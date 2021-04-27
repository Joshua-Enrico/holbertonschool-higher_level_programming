#!/usr/bin/python3
print("Lowercase Alphabets are:")
for a in range(97, 123):
    if chr(a) != 'e' and chr(a) != 'q':
        print(chr(a), end='')
