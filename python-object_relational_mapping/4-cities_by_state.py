#!/usr/bin/python3
"""a script that lists all cities from the database"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password_sys = sys.argv[2]
    database_name = sys.argv[3]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password_sys,
        database=database_name
    )
    c = db.cursor()
    c.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id
    """)
    states = c.fetchall()
    for state in states:
        print(state)
    c.close()
    db.close()
