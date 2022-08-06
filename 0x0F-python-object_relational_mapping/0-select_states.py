#!/usr/bin/python3
""" Module to print Mysql table """

import MySQLdb
import sys

db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                     password=sys.argv[2], database=sys.argv[3])
cur = db.cursor()

cur.execute("SELECT * FROM states")
result = cur.fetchall()

for row in result:
    print(row)
