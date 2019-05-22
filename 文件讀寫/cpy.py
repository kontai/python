#coding=utf-8
import os
import io

io.DEFAULT_BUFFER_SIZE=600

old_file=open("bak","r",encoding='utf-8',buffering=500)
new_file=open("clone.txt","w",encoding='utf-8')
big_file=open("clone.txt","w",encoding='utf-8')

old=old_file.read()
new_file.write(old)

#當讀取大檔案時,如果一次讀取,內存無法儲存,需要分批讀寫
while True:
    content = old_file.read(1024) #一次讀寫1kb
    if len(content)==0:           #當讀到末尾,跳離迴圈
        break
    big_file.write(content)
'''
#每個字符後面添加一個char
new_file2=open("clone2.txt","w",encoding='utf-8')
lenth=len(old)
for i in range(0,lenth):
    new_file2.write(old[i]+(chr)((i+98) if (i//113==0)else(i%113+98)))
'''



old_file.close()
new_file.close()
#new_file2.close()



