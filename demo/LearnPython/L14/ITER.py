# default string
L=[1]
I=iter(L)
print(next(I,'end of list'))
print(next(I,'end of list'))

I=iter(L)
while(x := next(I,None))!=None:
    print(x**2,end=' ')

