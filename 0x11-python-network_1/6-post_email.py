#!/usr/bin/python3
""" Sends POST request """

import requests
import sys

if __name__ == '__main__':

    data = dict(email=sys.argv[2])

    response = requests.post(sys.argv[1], data=data)
    print(response.text)
