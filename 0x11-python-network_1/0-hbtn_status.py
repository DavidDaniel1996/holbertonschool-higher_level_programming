#!/usr/bin/python3
""" Module that fetches a url """

import urllib.request

request = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(request) as f:
    body = f.read()
    print('Body Response:')
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf content: {body.decode('utf-8')}")

if __name__ == '__main__':
    pass
