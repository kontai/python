import redis

'''
    串列只能存放字串
    當首次插入的動作時,就會建立串列
'''

conn=redis.Redis()

# lpush  在開頭插入
conn.lpush('zoo','bear')

# 開頭插入兩個以上的項目
conn.lpush('zoo','alligator','duck')

# linsert 於指定鍵前/後 插入項目
conn.linsert('zoo','before','bear','beaver')
conn.linsert('zoo','after','bear','cassowary')

# lset 於指定位置插入(串列必須存在)
conn.lset('zoo',3,'marmoset')

# rpush 在尾端插入
conn.rpush('zoo','yak')

# lindex 利用索引取值
print(conn.lindex('zoo',3))

# lrange 取得範圍內的值
print(conn.lrange('zoo',0,-1))
    # l_all=dict(enumerate(conn.lrange('zoo',0,-1),0))
    # print(l_all)

# ltrim 修剪串列 (只保留指定範圍內的)
conn.ltrim('zoo',1,4)
print(conn.lrange('zoo',0,-1))




