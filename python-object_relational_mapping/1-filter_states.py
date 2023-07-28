#!/usr/bin/python3
"""task 1"""
import MySQLdb
import sys
"""
lists all states with a name starting with N (upper N) from the database
hbtn_0e_0_usa
"""

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    rows = cur.fetchall()
    for x in rows:
        print(x)
    db.close()
