import time

import redis

conn = redis.Redis()

key = 'now you see it'
conn.set(key, 'but not for long')

# 設置有效時間
conn.expire(key, 5)

# 印出有效時間
print(conn.ttl(key))

print(conn.get(key))

time.sleep(5)

print(conn.get(key))

