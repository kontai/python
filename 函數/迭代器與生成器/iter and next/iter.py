L=[1,2,3]
I=iter(L)
print(next(I))
print(next(I))
print(next(I))
# print(I.__next__())
# print(I.__next__())
# print(I.__next__())
# print(I.__next__()) #到達文件末尾，會出現StopIteration錯誤

f=open("1.txt",'w')     #文件對象本身就是自己的迭帶器 (有__next__()方法)
print(iter(f) is f)

print(iter(L) is L)