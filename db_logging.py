import sqlite3 as sq

con = sq.connect('reg.sqlite')
cur = con.cursor()

async def db_start_reg():
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
                       id serial PRIMARY KEY,
                       username VARCHAR NOT NULL,
                       password VARCHAR NOT NULL       
                       )''')
    con.commit()

#async def add_records_on_users():


cur.close()
