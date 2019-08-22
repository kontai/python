s1='abc'
s2='1234'
s3='spam'*4

def mymap(*seq,pad=None):
    seq=[list(x) for x in seq]
    res=[]
    while any(seq):
        res.append(tuple((S.pop(0) if S else pad)for S in list(seq)))
    return res

print(mymap(s1,s2))
print(mymap(s1,s2,s3))
U=mymap(s1,s2,s3)
a=[]
b=[]
c=[]

# print(list(map(a.,y,z for x in U.)))
list((a.append(x[0]),b.append(x[1]),c.append(x[2])) for x in U if None not in x)
print(a)
print(b)
print(c)

