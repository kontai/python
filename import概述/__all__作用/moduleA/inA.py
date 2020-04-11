import time
import datetime


def runA():
    a = time.time()
    print("inA.runA()," , a)

def runB():
    print("inA.runB,",datetime.time())

def runC():
    print("inA.runC,you can't see this ,because __all__ not include funC")
