import os
import sys

map1={"dirname":'abc','path':'c:\\dir\\a'}
print(map1['path'])
print(map1.get('path'))
print(os.path.basename(os.path.dirname(__file__)))
print(os.path.dirname(__file__))

dirname='demo22'
if not os.path.exists(dirname):
    os.mkdir(dirname)
    print('folder',dirname,'created!')
else:
    print(dirname,"is exist.")
