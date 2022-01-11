import redis

rs = redis.Redis()
# rs.hmset('test',{'count':1,'name':'Fester Bestertester'})

print(rs.hgetall('test'))

rs.hincrby('test','count',1)

print(rs.hgetall('test'))
