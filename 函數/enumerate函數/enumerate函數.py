# S='spam'
# offset=0
# for item in S:
#     print(item,'appears at offset',offset)
#     offset+=1

#using rnumerate

S='spam'
enumS=enumerate(S)
offset=0
for (offset,item) in enumerate(S):
    print(item,'appears at offset',offset)
    print(next(enumS)) #調用__next__方法 , 返回(index,value)元祖

print([c*i for (i,c) in enumerate(S)])
