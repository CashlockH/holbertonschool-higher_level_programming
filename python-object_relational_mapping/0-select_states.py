#!/usr/bin/python3
import MySQLdb
import sys
username_sys = sys.argv[1]
password_sys = sys.argv[2]
database_name = sys.argv[3]
db=MySQLdb.connect(host="localhost", port=3306, user = username_sys, password=password_sys, database=database_name)
c = db.cursor()
c.execute("""SELECT id, name FROM states ORDER BY id""")
c.fetchall()
c.close()
db.close()
