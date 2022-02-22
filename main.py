import sqlite3

#Establish connection and create cursor
conn = sqlite3.connect('database.db')
cur = conn.cursor()

#Execute SQL
cur.execute("SELECT * FROM ips WHERE asn==198 ORDER BY asn")
print(cur.fetchall())
