import sqlite3 as sql
import csv

db = sql.connect('books.db')
conn = db.cursor()
conn.execute('''
    CREATE TABLE books(
        title text,
        author text,
        year int
        )
''')
# sql_ins = 'INSERT INTO books(title,author,year) VALUES(?,?,?)'
# with open("books.csv", 'r') as f:
#     books = csv.DictReader(f)
#     for book in books:
#         conn.execute(sql_ins, book)
# conn.execute("SELECT * FROM books")
# print(conn.fetchall())
db.commit()
# conn.close()
