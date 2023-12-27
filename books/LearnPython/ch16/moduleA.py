# python

# from ch16 import moduleB
# import moduleB

# moduleB.foo()
print("moduleA start up")

# tuple([1,2,3],(1,4))

with open("moduleB.py","r") as mb:
    print(mb.readlines())

num=0
for f in open("moduleB.py","r"):
    # print(num,f,end='')
    print(num,f.rstrip())
    num+=1
