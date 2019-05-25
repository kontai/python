#------一般做法------------------
# dic={'abc':'string'}
# f=open('temp','w')
# f.write(str(dic))
# f.flush()
# f_read=open('temp','r')
# new_dic=eval(f_read.read())
# print(type(new_dic),',',new_dic)
#-------------------------------

import json

# dic2={'def':'dic'}
# dic2=json.dumps(dic2)
# print(type(dic2),',',dic2)
# f=open('temp','w')
# f.write(dic2)
# f.flush()

f_read=open("temp",'r')
new_dic2=f_read.read()
print(type(new_dic2),',',new_dic2)
new_dic2=json.loads(new_dic2)
print(type(new_dic2),',',new_dic2)

#pickle 用法與json一樣,只是json處理為字符串，而pickle處理為 byte
import pickle

dic_p={"sdf":23,"df":"sd","j3i":223}
dicii=pickle.dumps(dic_p)
print(type(dicii),',',dicii)

dicii=pickle.loads(dicii)
print(type(dicii),',',dicii)
