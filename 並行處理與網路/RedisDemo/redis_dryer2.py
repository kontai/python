from multiprocessing import freeze_support

def dryer():
    import redis
    import os
    import time
    conn = redis.Redis()
    pid = os.getpid()
    timeout = 20
    print("Dryer process %s is starting" % pid)
    while True:
        msg = conn.blpop('dishes', timeout)
        if not msg:
            break
        val = msg[1].decode('utf-8')
        if val == 'quit':
            break
        print('%s: dried %s' % (pid, val))
        time.sleep(0.1)
    print('Dryer process %s is done' % pid)

import multiprocessing

DRYER = 3
for num in range(DRYER):
    p = multiprocessing.Process(target=dryer,args=(DRYER,))
    p.start()
