import tornado as tornado

a=[1,2,3,4]
b=a
a[0]="abc"
print(a)
print(b)

b=a.copy()
a[1]="abc"
print(a)
print(b)

c=list(a)
print(c)

d=a[::]
print(d)
e=a,
print(e)

print(tuple(a))