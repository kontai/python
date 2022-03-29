import threading
import time


during_time=time.time()
class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n=n
    def run(self):
        print(threading.Thread.getName(self),self.n)
        time.sleep(2)

if __name__=="__main__":
    l=[]
    for i in range(50):
        t=MyThread(i)
        t.setDaemon(True)   #守護線程
        t.start()
        l.append(t)
    # for i in l:
    #     i.join()
    print("main is done")
    print("executing progress time=",time.time()-during_time)
