import csv

file=open('book.csv','w')
text='''
author,book
J R R Tolklen Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
'''
file.write(text)
file.flush()
file.close()