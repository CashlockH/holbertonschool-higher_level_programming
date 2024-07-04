#!/usr/bin/python3
""" a script that takes in the
name of a state as an argument and lists all cities of that state"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password_sys = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    if "'" in state_name:
        state_name = state_name.replace("'", "")
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password_sys,
        database=database_name
    )
    c = db.cursor()
    c.execute("""
        SELECT cities.name
        FROM cities
        INNER JOIN states
        ON states.id = cities.state_id
        WHERE states.name = '{}'
        ORDER BY cities.id
    """.format(state_name))
    cities = c.fetchall()
    for index, city in enumerate(cities):
        if index < len(cities) - 1:
            print(city[0], end=", ")
        else:
            print(city[0])
    c.close()
    db.close()
