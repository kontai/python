import sys
import time

list1 = ["1", "2", "3"]

# print(list1)
# print("\n".join(list1))
i=0

def wr(i):
    sys.stdout.write(i)
    
while i<len(list1):
    wr(list1[i])
    time.sleep(2)
    i+=1
