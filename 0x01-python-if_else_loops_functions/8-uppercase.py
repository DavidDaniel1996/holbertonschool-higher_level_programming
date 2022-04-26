#!/usr/bin/python3
def uppercase(str):
    str2 = ''
    for i in range(len(str)):
        ch = ord(str[i])
        if ch >= 97 and ch <= 123:
            str2 += chr(ch - 32)
        else:
            str2 += chr(ch)
    print(str2)
