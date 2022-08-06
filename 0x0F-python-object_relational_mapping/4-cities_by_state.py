#!/usr/bin/python3
"""Module to print Mysql table"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()

    cur.execute("""
    SELECT
        cities.id, cities.name, states.name
    FROM
        cities
    INNER JOIN
        states
    ON
        cities.state_id=states.id
        """)
    result = cur.fetchall()

    for row in result:
        print(row)
