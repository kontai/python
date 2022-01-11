import sqlalchemy as sa
#SQLAlchemy 引擎室

# 建立連結
# 於記憶體創建資料庫
# METHOD 1
# :memory: 將資料庫儲存於記憶體內
# conn=sa.create_engine('sqlite:///:memory:')

# METHOD 2
conn = sa.create_engine('sqlite://')
result = conn.execute('''CREATE TABLE zoo
            (critter VARCHAR(20) PRIMARY KEY,
            count INT,
            damages FLOAT)''')

ins = "INSERT INTO zoo(critter,count,damages) VALUES (?,?,?)"
conn.execute(ins, 'duck', 10, 0.0)
conn.execute(ins, 'bear', 2, 1000.0)
conn.execute(ins, 'weasel', 1, 2000.0)
rows = conn.execute('SELECT * FROM zoo')

for i in rows:
    print(i)