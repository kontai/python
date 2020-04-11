# 函數在每次循環都會產生一個值，之後將其返回給他的調用者
#1
import time

count=5000000

def gensquares(N):
    for i in range(N):
        yield i ** 2

start_time=time.time()
for i in gensquares(count):
    pass
    # print(i, end=' : ')
print('\t','* gensquares() 花費時間:',time.time()-start_time,'\n')

#2
def buildsquares(n):
    res = []
    for i in range(n): res.append(i ** 2)
    return res
start_time=time.time()
for x in buildsquares(count):pass# print(x, end=' : ')
print('\t','* builssquares() 花費時間:',time.time()-start_time,'\n')

#3
start_time=time.time()
for n in [i ** 2 for i in range(count)]:
    pass
    # print(n, end=' : ')
print('\t','* for函式生成器 花費時間:',time.time()-start_time,'\n')

#4
start_time=time.time()
for n in map((lambda x: x ** 2), range(count)):
    pass
    # print(n, end=' : ')
print('\t','* map函式生成器 花費時間:',time.time()-start_time,'\n')
