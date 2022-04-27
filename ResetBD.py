import sqlite3

con = sqlite3.connect(r"C:\...\NomeFonte\...explorer.db")

cur = con.cursor()

# cur.execute(f'DELETE FROM arquivos')
# cur.execute(f'DELETE FROM sqlite_sequence')
cur.execute(f'DELETE FROM dependencias')

con.commit()