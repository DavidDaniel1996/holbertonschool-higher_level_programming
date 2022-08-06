#!/usr/bin/python3

import MySQLdb

db = MySQLdb.connect(host='localhost', username='root',
                     password='root', database='hbtn_0e_0_usa')
cur = db.cursor()

cur.execute("SELECT * FROM states")
result = cur.fetchall()

for row in result:
    print(row)
