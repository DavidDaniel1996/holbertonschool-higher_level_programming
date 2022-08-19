#!/usr/bin/python3
""" Module that fetches a url """

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as f:
        body = f.read()
        print("Body Response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf content: {}".format(body.decode("utf-8")))
