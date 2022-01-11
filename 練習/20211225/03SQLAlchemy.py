import sqlalchemy as sa

conn = sa.create_engine('sqlite:///books.db')
sql='SELECT title FROM books order by title'
books=conn.execute(sql)
for book in books:
    print(book)