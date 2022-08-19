#!/usr/bin/python3
""" Display body of url response after request """

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            response_text = response.read()
            print(response_text.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print(error.code)
