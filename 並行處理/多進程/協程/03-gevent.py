# import queue


import gevent
import requests, time

start = time.time()


def f(url):
    print('GET: %s' % url)
    resp = requests.get(url)
    data = resp.text
    print('%d bytes received from %s.' % (len(data), url))


f('https://www.python.org/')
f('https://www.yahoo.com/')
f('https://www.baidu.com/')
f('https://www.sina.com.cn/')
f("http://www.xiaohuar.com/hua/")

# gevent.joinall([
#         gevent.spawn(f, 'https://www.python.org/'),
#         gevent.spawn(f, 'https://www.yahoo.com/'),
#         gevent.spawn(f, 'https://www.baidu.com/'),
#         gevent.spawn(f, 'https://www.sina.com.cn/'),
#         gevent.spawn(f, 'http://www.xiaohuar.com/hua/'),
# ])

# f('https://www.python.org/')
#
# f('https://www.yahoo.com/')
#
# f('https://baidu.com/')

# f('https://www.sina.com.cn/')

print("cost time:", time.time() - start)
