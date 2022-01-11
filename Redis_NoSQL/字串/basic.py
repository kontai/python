import redis

# 字串
'''
    字串有一個鍵,一個值
    簡單的python資料類型會被自動轉換
    連結到伺服器的主機(預設是localhost) 與連接埠(預設是6379)
'''

# redis.Redis('localhost')與 redis.Redis('localhost',6379)相同
conn = redis.Redis()

# 列出所有的鍵
conn.keys()

# set 設定值
conn.set('secret', 'nil')
conn.set('carats', 24)
conn.set('fever', '101.5')

#get 取值
secret = conn.get('secret')
carats = conn.get('carats')
fever = conn.get('fever')
print(secret, fever, carats)

#setnx 當健不存在就賦值
conn.setnx('secret',66)
print(conn.get('secret'))

#getset 返回舊值,並設定新值
get_set=conn.getset('secret','icky-icky-icky-ptang-zoop-boing')
print('old = %s\nnew = %s'%(get_set,conn.get('secret')))

#getrange 取得一個子字串
sub_str1=conn.getrange('secret',-5,-1)
print(sub_str1)

#setrange 替換一個子字串
rep_str1=conn.setrange('secret',0,'ICXY')
print(conn.get('secret'))

#mset 一次設定多個值
conn.mset({'pie':'cherry','cordial':'sherry'})

#mget   一次取得多個值
print(conn.mget('pie','cordial'))

#delete 刪除
conn.delete('fever')

#incr 與 incrbyfloat 遞增 , decr 遞減
print(conn.get('carats'))
print(conn.incr('carats'))
print(conn.incr('carats',10))
print(conn.decr('carats'))
print(conn.decr('carats',10))

print(conn.set('fever','101.5'))
print(conn.incrbyfloat('fever'))
print(conn.incrbyfloat('fever',0.5))
print(conn.incrbyfloat('fever',-2.5))   #沒有減法,利用負值做減法


