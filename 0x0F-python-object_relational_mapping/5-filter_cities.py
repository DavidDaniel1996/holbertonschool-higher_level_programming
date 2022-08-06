#!/usr/bin/python3
"""Module to print rows with specific name"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    cur.execute("""
            SELECT
                cities.name
            FROM
                cities
            INNER JOIN
                states
            ON
                cities.state_id=states.id
            WHERE
                states.name = %(state_name)s
        """, {
            'state_name': sys.argv[4]
        })

    result = cur.fetchall()

    if not result:
        print()
    for i, cities in enumerate(result):
        if i == len(result) - 1:
            print("{}".format(str(cities[0])))
        else:
            print("{}, ".format(str(cities[0])), end="")
