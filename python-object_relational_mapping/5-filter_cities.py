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
        SELECT *
        FROM cities
        INNER JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id
    """)
    cities = c.fetchall()
    city_list = []
    for city in cities:
        if city[4] == state_name:
            city_list.append(city[2])
    for index, city in enumerate(city_list):
        if index < len(city_list) - 1:
            print(city, end=", ")
        else:
            print(city)
    c.close()
    db.close()
