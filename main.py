import sqlite3
import pandas

#Establish connection and create cursor
conn = sqlite3.connect('database.db')
cur = conn.cursor()

#Execute SQL
#cur.execute("SELECT * FROM ips WHERE asn==198 ORDER BY asn")
#print(cur.fetchall())

#Converting SQl to CSV
df = pandas.read_sql_query("SELECT * FROM ips", conn)
print(df)

df.to_csv("database1.csv", index = None)
#df.to_excel("database2.xlsx")
