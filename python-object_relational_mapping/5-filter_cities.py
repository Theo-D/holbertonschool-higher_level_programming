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
    cnx.execute("SELECT cities.name FROM cities " \
    "JOIN states ON cities.state_id = states.id" \
    " WHERE states.name = %s ORDER BY cities.id;",(state_name,))

    res = cnx.fetchall()
    for i in range(len(res)):
        if i < len(res) - 1:
            print(res[i][0], end=", ")
        else:
            print(res[i][0], end="\n")

    cnx.close()
    db.close()
