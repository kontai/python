import sqlite3 as sql

db = sql.connect('books.db')
conn = db.cursor()
conn.execute('SELECT title FROM books ORDER BY title ASC')
books=conn.fetchall()
for book in books:
    print(book)