import sqlite3

con = sqlite3.connect(r"C:\...\NomeFonte\...explorer.db")

cur = con.cursor()

print(cur.execute('SELECT * FROM arquivos'))
cur.fetchall()

