import threading
import time
'''同步鎖'''
num=100
def sub():
    global num
    lock.acquire()
    temp=num
    time.sleep(0.01)
    num=temp-1
    lock.release()

list=[]

lock=threading.Lock()
for i in range(100):
    t1 = threading.Thread(target=sub)
    t1.start()
    list.append(t1)

for i in list:
    i.join()
print(num)