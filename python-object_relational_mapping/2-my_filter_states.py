#!/usr/bin/python3
"""Filtering state query with input"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password_sys = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
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
        WHERE name = %s
        ORDER BY states.id
    """, (state_name,))
    states = c.fetchall()
    for state in states:
        print(state)    
    c.close()
    db.close()
