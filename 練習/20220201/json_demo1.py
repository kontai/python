import json
import pickle

f=open('01','w')
map1={"A":1,"B":2,"C":3}
data1=json.dumps(map1)
# print(data1)
# print(type(data1))
json.dump(data1,f)


def Demo1():
    return 2

with open('pk1.txt','wb') as file:
    # pk1=pickle.dumps(data1)
    pk1=pickle.dumps(Demo1)
    file.write(pk1)


with open('pk1.txt','rb') as file:
    data2=pickle.load(file)

print(data2())

