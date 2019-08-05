'''
range手動產生的迭代對象，各自記住自己的位置
'''
print("-"*10,range,"-"*10)
R=range(3)
I1=iter(R)
print(next(I1))
print(next(I1))

I2=iter(R)
print(next(I2))
print(next(I2))

print(next(I1))

'''
map、zip、filter不支持
'''
print("-"*10,zip,"-"*10)
Z=zip((1,2,3),(4,5,6))
I1=iter(Z)
I2=iter(Z)
print(next(I1))
print(next(I2))

print("-"*10,map,"-"*10)
M=map(abs,(-1,0,2))
I1=iter(M);I2=iter(M)
print(next(I1),next(I1),next(I2))
try:
    print(next(I2))
except:
    StopIteration()

