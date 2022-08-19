#!/usr/bin/python3
""" POST requests to url """

from urllib import request, parse
import sys

if __name__ == '__main__':

    email = {'email': sys.argv[2]}

    query_string = parse.urlencode(email)
    data = query_string.encode('ascii')

    with request.urlopen(sys.argv[1], data) as response:
        response_text = response.read()
        print(response_text)
