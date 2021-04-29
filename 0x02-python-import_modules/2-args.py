#!/usr/bin/python3
if __name__ == '__main__':
    import sys
if len(sys.argv) == 1:
    print(0, 'arguments:')
else:
    print(len(sys.argv) - 1, 'arguments:')
    for a in range(1, len(sys.argv)):
        print('{}:'.format(a), sys.argv[a])
