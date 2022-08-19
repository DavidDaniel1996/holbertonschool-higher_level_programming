#!/usr/bin/python3
""" Displays value of X-Request-ID """

import requests
import sys

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
