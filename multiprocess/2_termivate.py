import multiprocessing

import multiprocessing
import os
import time


def whoami(name):
    print("I'm %s, in process %s" % (name, os.getpid()))


def loopy(name):
    whoami(name)
    start = 1
    stop = 1000000
    for num in range(start, stop):
        print("\tNumber %s of %s ,Honk!" % (num, stop))
        time.sleep(1)

def loopy2(name):
    whoami(name)
    start = 1
    stop = 1000000
    for num in range(start, stop):
        print("\tNumber %s of %s ,Honk!" % (num, stop))
        time.sleep(1)

if __name__ == '__main__':
    whoami("main")
    p = multiprocessing.Process(target=loopy, args=('loopy',))
    p1 = multiprocessing.Process(target=loopy2, args=('pyloop',))
    p.start()
    p1.start()

    time.sleep(5)
    p.terminate()
    time.sleep(5)
    p1.terminate()
