#!/usr/bin/python3
""" Sends POST request """

if __name__ == '__main__':
    import requests
    import sys

    data = dict(email=sys.argv[2])

    response = requests.post(sys.argv[1], data=data)
    print(response.text)
