import threading
import time

def music():
    print("playing music... %s"% time.strftime("%H:%M:%S",time.localtime()))
    time.sleep(3)
    print("stop music... %s"% time.strftime("%H:%M:%S",time.localtime()))

def movies():
    print("playing movies... %s"% time.strftime("%H:%M:%S",time.localtime()))
    time.sleep(5)
    print("stop movies... %s"% time.strftime("%H:%M:%S",time.localtime()))

if __name__ == '__main__':
    t1=threading.Thread(target=music,args=())
    t2=threading.Thread(target=movies,args=())

    t1.start()
    t2.start()

    # t1.join()
    # t2.join()
    print("end....")
