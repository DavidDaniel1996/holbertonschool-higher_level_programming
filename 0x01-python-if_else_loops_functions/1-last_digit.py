#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    bufnumber = number * -1
else:
    bufnumber = number

if bufnumber % 10 > 5:
    print("The Last digit of {:d} is {:d} and is greater than 5"
          .format(number, bufnumber % 10))
elif number % 10 < 6 and number % 10 != 0:
    print("The Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, bufnumber % 10))
else:
    print("The Last digit of {:d} is {:d} and is 0"
          .format(number, bufnumber % 10))
