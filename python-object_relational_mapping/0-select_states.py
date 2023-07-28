#!/usr/bin/python3
"""task 0"""
import MySQLdb
import sys


if __name__ == "__name__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for x in rows:
        print(x)
    db.close()
