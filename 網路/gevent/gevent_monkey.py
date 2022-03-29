import gevent
from gevent import monkey
import socket

#任何呼叫一般的socket的地方插入gevent通訊端
# monkey.patch_socket()
monkey.patch_all()

hosts = ['www.trappytaxidermy.com', 'www.walterposttertacldermy.com',
         'www.antlque-taxidermy.com','www.google.com']
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs,timeout=5)
for job in jobs:
    print(job.value)
