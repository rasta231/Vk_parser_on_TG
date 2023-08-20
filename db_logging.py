import sqlite3 as sq

con = sq.connect('reg.sqlite')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username VARCHAR,
               password VARCHAR
               )''')
con.commit()




cur.close()
