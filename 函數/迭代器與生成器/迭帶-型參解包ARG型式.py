def f(a,b,c,d,*arg):
    print(a,b,c,d,*arg,sep="%")

f(1,2,3,4)

f(*[4,5,6,7])

# f(*open('zip.py'))

X=(1,2)
Y=(3,4)
list(zip(X,Y))
A,B=zip(*zip(X,Y))
print(A,B)

print(sum(range(1,100)))
