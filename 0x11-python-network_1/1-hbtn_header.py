#!/usr/bin/python3
""" Module displays 'X-Request-ID' header """

import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as f:
    print(f.getheader('X-Request-Id'))
