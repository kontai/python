import gevent
from gevent import socket

hosts = ['www.trappytaxidermy.com', 'www.walterposttertacldermy.com',
         'www.antlque-taxidermy.com','www.google.com']
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs,timeout=5)
for job in jobs:
    print(job.value)
