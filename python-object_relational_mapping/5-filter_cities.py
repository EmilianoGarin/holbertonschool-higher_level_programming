#!/usr/bin/python3
"""task 5:
takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    ck = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    if not all(c in ck for c in sys.argv[4]):
        exit()

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    txt = "SELECT cities.name FROM cities\
           JOIN states ON state_id = states.id\
           WHERE states.name LIKE '%{0}%'\
           ORDER BY cities.id".format(sys.argv[4])
    cur.execute(txt)
    rows = cur.fetchall()
    db.close()

    row = []
    for x in rows:
        row += x
    print(", ".join(row))
