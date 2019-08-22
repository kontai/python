L1=[1,2,3,4]
L2=[5,6,7,8]
print(zip(L1,L2))
print(list(zip(L1,L2)))

for (x,y) in zip(L1,L2):
    print(x,y,'--',x+y)

T1,T2,T3=(1,2,3),(4,5,6),(7,8,9)
print(list(zip(T1,T2,T3)))

S1='abc'
S2='xyz123'
print(list(zip(S1,S2)))   #會以最短序列長度為準 來截斷所得的長度。



