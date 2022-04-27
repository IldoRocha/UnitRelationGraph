import sqlite3

con = sqlite3.connect(r"C:\...\NomeFonte\...explorer.db")

cur = con.cursor()

cur.execute('CREATE TABLE dependencias(codigo INTEGER PRIMARY KEY, arquivo INTEGER, UsesInterface VARCHAR(1000), UsesImplementation VARCHAR(1000))')

con.commit()

con.close()