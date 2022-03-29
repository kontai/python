import threading
import time


def demo(num):
    print("number=", num)
    time.sleep(2)


class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        self.n = n

    def run(self):
        print("runnint task", self.n)


if __name__ == "__main__":
    t1 = threading.Thread(target=demo, args=("t1",))
    t2 = threading.Thread(target=demo, args=("t2",))
    t1.start()
    t2.start()
    t2.join()

