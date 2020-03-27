import sqlite3

serverID = 522808209959026690

conn = sqlite3.connect('RomeBot.db')
c = conn.cursor()
c.execute("SELECT features FROM servers WHERE serverID = {}".format(serverID))
print(c.fetchall())
conn.commit()
conn.close()