#!/usr/bin/python3
"""task 1"""
import MySQLdb
import sys
"""
takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states\
                WHERE name = '{sys.argv[4]}'\
                ORDER BY id")
    rows = cur.fetchall()
    for x in rows:
        print(x)
    db.close()
