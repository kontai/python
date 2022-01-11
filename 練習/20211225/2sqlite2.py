import csv
import sqlite3 as sql

db = sql.connect('books.db')
conn = db.cursor()
with open('books.csv', 'r') as f:
    sql = 'INSERT INTO books(title,author,year) VALUES(?,?,?)'
    books=csv.DictReader(f)
    for book in books:
        # print(book)
        conn.execute(sql,(book['title'],book['author'],book['year']))
db.commit()
