import redis

conn=redis.Redis()
print("Washer is starting")
dishes=['salad','bread','entree','dessert']
num=0
for dish in dishes:
    msg=dish.encode('utf-8')
    conn.rpush('dishes',msg)
    num+=1
    print('Washed',num)
conn.rpush('dishes','quit')
print('Washer is done')
