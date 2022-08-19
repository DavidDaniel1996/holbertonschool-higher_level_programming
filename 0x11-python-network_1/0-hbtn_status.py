#!/usr/bin/python3
""" Module that fetches a url """

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as f:
    body = f.read()

print('Body Response:')
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")
print(f"\t- utf content: {body.decode('utf-8')}")
