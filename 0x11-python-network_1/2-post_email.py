#!/usr/bin/python3
""" POST requests to url """

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':

    email = {'email': sys.argv[2]}

    query_string = urllib.parse.urlencode(email)
    data = query_string.encode('ascii')

    with urllib.request.urlopen(sys.argv[1], data) as response:
        response_text = response.read()
        print(response_text.decode('utf8'))
