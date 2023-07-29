#!/usr/bin/python3
"""task 2:
takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    ck = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    if not all(c in ck for c in sys.argv[4]):
        exit()
    txt = "SELECT * FROM states \
           WHERE name LIKE '%{0}%' \
           ORDER BY id".format(sys.argv[4])
    cur.execute(txt)
    rows = cur.fetchall()
    for x in rows:
        print(x)
    db.close()
