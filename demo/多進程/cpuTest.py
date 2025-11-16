import multiprocessing
import os
import time


def task1():
    for i in range(1000):
        # print(os.getpid(), "is running..")
        # print(multiprocessing.current_process())
        time.sleep(0.05)
    print(f'{multiprocessing.current_process()} done.')


if __name__ == '__main__':
    sub_proc = multiprocessing.Process(target=task1)
    sub_proc2 = multiprocessing.Process(target=task1)
    sub_proc3 = multiprocessing.Process(target=task1)
    sub_proc4 = multiprocessing.Process(target=task1)
    sub_proc5 = multiprocessing.Process(target=task1)
    sub_proc.start()
    sub_proc2.start()
    sub_proc3.start()
    sub_proc4.start()
    sub_proc5.start()
    sub_proc.join()
    sub_proc2.join()
    sub_proc3.join()
    sub_proc4.join()
    sub_proc5.join()
    print("all done")
