# coding:utf-8
import time
from concurrent.futures import ThreadPoolExecutor
import threading

locks = threading.Lock()


'''
演示线程池的使用
'''
def work(arg):
    # with locks:
    locks.acquire()
    print(arg)
    time.sleep(1)
    locks.release()


if __name__ == "__main__":
    pool = ThreadPoolExecutor(2)
    for p in range(20):
        pool.submit(work, p)
    pool.shutdown()
    print("Done")
