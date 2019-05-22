# -*- coding: UTF-8 -*-
old_file=open("clone.txt")
file_loc=old_file.tell()
print("文件位置=> %d"%file_loc)

old=old_file.read(10)
print(old)
file_loc=old_file.tell()  #查詢文件指標位置
print("文件位置=> %d"%file_loc)

old=old_file.read(10)
print(old)
file_loc=old_file.tell()
print("文件位置=> %d"%file_loc)

print('*'*100)

'''
Python文件的tell()方法返回文件中的文件读/写指针的当前位置。

seek()方法的语法 -
fileObject.seek(offset[, whence])
参数
    ＠offset − 这是文件中读/写指针的位置。
    ＠whence − 这是可选的，默认为0，表示绝对文件定位，其他值为1，这意味着相对于当前位置进行搜索，2表示相对于文件的末尾进行搜索。
'''
old_file.seek(0,0)
file_loc=old_file.tell()
print("重置文件指標後,文件位置=> %d"%file_loc)

old=old_file.read(10)
file_loc=old_file.tell()
print(old)
print("文件位置=> %d"%file_loc)
