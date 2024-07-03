import MySQLdb
import sys
if __name__ = "__main__":
    username = sys[1]
    password_sys = sys[2]
    database_name = sys[3]
    db = MySQLdb.connect(
        host="localhost",
        port = 3306,
        user = username,
        password = password_sys,
        database = database_name
        )
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id""")
    states = c.fetchall()
    for state in states:
        print(state)
    c.close()
