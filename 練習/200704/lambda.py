
'''
name='alex'
u=(lambda x:x+'_sb')
print(u(name))
'''

x='abc'
y='bcd'
z='adf'
a=[1,2,3]

# b=list(map(lambda x:x+1,list(range(20))))
# b=(lambda x:x*x)
def foo(x):
    b=[]
    print(x)
    if(len(x)>1):
        for i in x:
            b.append(i*i)
    return b


a=[1,2,10,5,3,7]
b=foo
c=list(map(b,a))
print('%-10s=>'%'sorted',sorted(c))

print('%-10s=>'%'unsorted',c)
