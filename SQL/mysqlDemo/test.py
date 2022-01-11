import mysql.connector as ms

conn = ms.connect(user='root', password='@@@@@', database='test')
try:
    cursor = conn.cursor()
    # cursor.execute('create table zoo(id varchar(20) primary key ,name varchar(20))')
    ins='insert into zoo (id,name) values(%s,%s)'
    cursor.execute(ins, ['3', 'John'])
    # cursor.execute('insert into zoo (id,name) values (%s,%s)',['2','Michael'])
    conn.commit()
except ms.errors:
    print(ms.errors.error)
finally:
    conn.close()
