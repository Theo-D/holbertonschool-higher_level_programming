#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cnx = db.cursor()
    # execute needs tuple to pass argument to query
    cnx.execute("SELECT * FROM states WHERE name = %s ORDER BY id",
                (state_name,))

    for row in cnx.fetchall():
        print(row)

    cnx.close()
    db.close()
