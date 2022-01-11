import re

file='gmail.txt'

fin=open(file,'r')
fout=open('out','w')

for i in range(10):
    # msg=fin.readline().split('----')
    msg=fin.readline().replace('----',' ')
    print(msg,file=fout)
    # print(msg.split('----'),file=fout)