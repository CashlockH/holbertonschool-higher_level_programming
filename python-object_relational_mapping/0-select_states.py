#!/usr/bin/python3
"""Mysql database"""
import MySQLdb
import sys
if __name__ == '__main__':
    username_sys = sys.argv[1]
    password_sys = sys.argv[2]
    database_name = sys.argv[3]
    db=MySQLdb.connect(host="localhost", port=3306, user = username_sys, password=password_sys, database=database_name)
    c = db.cursor()
    c.execute("""SELECT id, name FROM states ORDER BY id""")
    states = c.fetchall()
    for state in states:
        print(state)
    c.close()
    db.close()
