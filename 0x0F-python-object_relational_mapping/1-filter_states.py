#!/usr/bin/python3
"""Module to print stats with N"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states")
    result = cur.fetchall()
    char_match = set('N')

    for row in result:
        if row[1][0] in char_match:
            print(row)
