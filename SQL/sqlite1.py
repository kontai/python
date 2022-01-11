#!bin/env python3
import sqlite3

conn = sqlite3.connect("enterprise.db")  # 建立連接
curs = conn.cursor()  # 建立一個cursor物件
# curs.execute('''CREATE TABLE zoo
#     (critter VARCHAR(20) PRIMARY KEY,
#     count INT,
#     damage FLOAT )''')

# curs.execute('''INSERT INTO zoo VALUES("duck" , 5 , 0.0)''')
# ins="INSERT INTO zoo (critter,count,damage) VALUES (?,?,?)"
# curs.execute(ins,('weasel',1,2000))
# curs.execute('SELECT * FROM zoo ORDER BY critter DESC ')
curs.execute('SELECT * FROM zoo WHERE damage=(SELECT MAX(damage) FROM zoo)')
rows=curs.fetchall()
print(rows)
# rows=curs.fetchone()
# rows2=curs.fetchone()
# print(rows,rows2)
conn.commit()
