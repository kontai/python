'''
请先在 IDLE 中获得下边列表的结果，并按照上方例子把列表推导式还原出来。
1.	>>> list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
'''

list2=[]

for x in range(10):
    for y in range(10):
        if(x%2==0) and (y%2!=0):
            list2.append((x,y))

print(list2)
