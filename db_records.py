import asyncio
import sqlite3 as sq
from main import res_dict

con = sq.connect('reg.sqlite')
cur = con.cursor()


async def db_start():
    cur.execute('''CREATE TABLE IF NOT EXISTS records (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   chapter INT,
                   name VARCHAR,
                   url VARCHAR,
                   date_time VARCHAR
                   )''')
    con.commit()


async def add_record():
    for i in range(len(res_dict)):
        try:
            cur.execute("""INSERT INTO records (id, chapter, name, url, date_time) VALUES (?,?,?,?,?)""",
                        (i, res_dict[f'chapter_{i}'], res_dict[f'name_{i}'], res_dict[f'url_{i}'],
                         res_dict[f'date_create{i}']))
            con.commit()
        except KeyError:
            continue


async def print_rec():
    records = []
    tmp = cur.execute('''SELECT * FROM records''')
    rows = tmp.fetchall()
    for row in rows:
        record = {
            'ID': row[0],
            'Chapter': row[1],
            'Name': row[2],
            'URL': row[3],
            'Date': row[4]
        }
        records.append(record)
    con.close()
    return records





