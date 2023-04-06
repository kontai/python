import threading
import time


class bgcolor:
    BGSTART = '\033[;46;31m'
    BG_FINISHED = '\033[31m'
    BGEND = '\033[0m'


def funA():
    print(bgcolor.BGSTART + "got A" + time.asctime() + bgcolor.BGEND)
    time.sleep(3)
    print(bgcolor.BG_FINISHED + "A Finished" + time.asctime() + bgcolor.BGEND)


def funB():
    print(bgcolor.BGSTART + "got B" + time.asctime() + bgcolor.BGEND)
    time.sleep(5)
    print(bgcolor.BG_FINISHED + "B Finished" + time.asctime() + bgcolor.BGEND)


if __name__ == '__main__':
    t1 = threading.Thread(target=funA)
    t2 = threading.Thread(target=funB)
    t1.setDaemon(True)
    t1.start()
    t2.start()
    # t1.join()
    # t2.join()
    # funA()
    # funB()

    print(bgcolor.BG_FINISHED + 'main finished' + time.asctime() + bgcolor.BGEND)
    # print("\033[;46;31m OK \033[0m")
