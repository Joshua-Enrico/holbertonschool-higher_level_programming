#!/usr/bin/python3
if __name__ == '__main__':
    import sys
if len(sys.argv) is 1:
    print(0, 'arguments.')
else:
    if len(sys.argv) is 2:
        print(len(sys.argv) - 1, 'argument:')
        print('{}:'.format(len(sys.argv) - 1), sys.argv[1])
    else:
        print(len(sys.argv) - 1, 'arguments:')
        for i in range(1, len(sys.argv)):
            print('{}:'.format(i), sys.argv[i])
