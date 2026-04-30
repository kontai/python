import time
from multiprocessing import Process


def w():
    with open("/tmp/1.txt", "w") as f:
        while (1):
            f.write("1")
            f.flush()
            time.sleep(1)


def r():
    with open("/tmp/1.txt", "r") as f:
        while (1):
            time.sleep(1)
            print(f.read())


if __name__ == "__main__":
    wp=Process(None,w)
    rp=Process(None,r)

    wp.start()
    rp.start()


