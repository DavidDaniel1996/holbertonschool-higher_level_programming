#!/usr/bin/python3
"""Module to print rows with specific name"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name = '{}'".format(sys.argv[4]))
    result = cur.fetchall()

    for row in result:
        print(row)
