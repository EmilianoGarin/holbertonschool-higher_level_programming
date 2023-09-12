#!/usr/bin/python3
"""task 4:
lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    txt = "SELECT cities.id, cities.name, states.name FROM cities\
           JOIN states ON state_id = states.id\
           ORDER BY id"
    cur.execute(txt)
    rows = cur.fetchall()
    for x in rows:
        print(x)
    db.close()
