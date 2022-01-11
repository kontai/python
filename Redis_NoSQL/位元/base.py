import redis

conn = redis.Redis()

days = ['2013-02-25', '2013-02-26', '2013-02-27']
big_spender = 1009
tire_kicker = 40459
late_joiner = 550212

conn.setbit(days[0], big_spender, 1)
conn.setbit(days[0], tire_kicker, 1)

conn.setbit(days[1], big_spender, 1)

conn.setbit(days[2], big_spender, 1)
conn.setbit(days[2], late_joiner, 1)

for day in days:
    print(conn.bitcount(day))

# conn.setbit(days[1],tire_kicker,0)
print(conn.getbit(days[1], tire_kicker))
