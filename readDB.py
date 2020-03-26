import sqlite3

conn = sqlite3.connect('RomeBot.db')
c = conn.cursor()
print(c.fetchall())
conn.commit()
conn.close()