#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = 0
    if len(argv) == 2:
        count += 1
        print("{:d} argument:".format(len(argv) - 1))
        print("{:d}:".format(count), argv[count])
    else:
        if len(argv) == 1:
            print("{:d} arguments.".format(len(argv) - 1))
        else:
            print("{:d} arguments:".format(len(argv) - 1))
            for i in range(0, len(argv) - 1):
                count += 1
                print("{:d}:".format(count), argv[count])
