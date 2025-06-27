#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

cities = []

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
    cnx.execute("SELECT cities.name FROM cities "
                "JOIN states ON cities.state_id = states.id"
                " WHERE states.name = %s ORDER BY cities.id;", (state_name,))

    res = cnx.fetchall()
    for elm in res:
        cities.append(elm[0])

    print(", ".join(cities))

    cnx.close()
    db.close()
