#!/usr/bin/python3
"""Filtering state query"""
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
        SELECT *
        FROM states
        ORDER BY states.id
    """)
    states = c.fetchall()
    for state in states:
        if state[1].startswith("N"):
            print(state)
    c.close()
    db.close()
