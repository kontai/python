import csv
# file_r=open("book.csv",'r')
with open("book.csv",'r') as fo:
    books=csv.DictReader(fo)
    for book in books:
        print(book)

