import redis

''' 
    Redis 的集合跟python很像
'''
conn = redis.Redis()

# sadd 將一個或多個值加入集合
conn.sadd('zoo','duck','turkey')

# scard 取得集合的數量
conn.scard('zoo')

# smember 取得集合所有的值
conn.smember('zoo')

# srem 移除集合的值
conn.srem('zoo','turkey')

# sinter 交集
conn.sadd('better_zoo','tiger','wolf','duck')
conn.sinter('zoo','better_zoo')

# 取得交集,並將結果存入集合fowl_zoo
conn.sinterstore('fowl_zoo','zoo','better_zoo')

# sunion 取得聯集(所有成員)
conn.sunion('zoo','better_zoo')

# sunionstore 將聯集存入fabulous_zoo集合
conn.sunionstore('fabulous','zoo','better_zoo')

# sdiff 集合的差異  sdiffstore 將差異存入zoo_sale
conn.sdiff('zoo','better_zoo')
conn.sdiffstore('zoo_sale','zoo','better_zoo')