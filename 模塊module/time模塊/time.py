import time

# 1 time() :返回当前时间的时间戳
print(time.time())  # 時間戳(from 1970)

# 2 localtime([secs])
# 将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。
print(time.localtime())  # 當地時間
print(time.localtime(time.time()))
print(time.localtime(1000000000))

# t=time.localtime()
# print(t.tm_year)

# 3 gmtime([secs]) 和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。
print(time.gmtime())  # UTC

# 4 mktime(t) : 将一个struct_time转化为时间戳。
print(time.mktime(time.localtime()))

# 6 ctime([secs]) : 把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为
# None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。
print(time.ctime())  # Sun Sep 11 00:46:38 2016

print(time.ctime(time.time()))  # Sun Sep 11 00:46:38 2016

# 7 strftime(format[, t]) : 把一个代表时间的元组或者struct_time（如由time.localtime()和
# time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。如果元组中任何一个
# 元素越界，ValueError的错误将会被抛出。
print(time.strftime("%Y-%m-%d %X", time.localtime()))  # 2016-09-11 00:49:56

# 8 time.strptime(string[, format])
# 把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。
print(time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X'))

# time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=16, tm_min=37, tm_sec=6,
#  tm_wday=3, tm_yday=125, tm_isdst=-1)

# 在这个函数中，format默认为："%a %b %d %H:%M:%S %Y"。


# 9 sleep(secs)
# 线程推迟指定的时间运行，单位为秒。

# 10 clock()
# 这个需要注意，在不同的系统上含义不同。在UNIX系统上，它返回的是“进程时间”，它是用秒表示的浮点数（时间戳）。
# 而在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行
# 时间，即两次时间差。
