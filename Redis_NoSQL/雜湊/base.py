from datetime import datetime

import redis

''' 
    Redis 雜湊與python 字典很像 ,但只能容納字串
    因此,你只能在下一層,舞法製作深層嵌套
'''

conn = redis.Redis()

# hmset 設定雜湊變量 song 的 do 與 re
# info = {'do': 'a deer', 're': 'about a deer'}
# conn.hset('song', 'amp',info)
print(datetime.utcnow().strftime('%Y-%m-%d %W%H:%M'))

# hset 設定單一欄位值
conn.hset('song', 'mi', 'a note to follow re')

# hget 取得一個欄位值
print(conn.hget('song', 'mi'))
