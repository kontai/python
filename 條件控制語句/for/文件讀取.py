#一次讀取整個文件
for line in open("test.txt").readline():
    print(line,end='')


# use iterators best text imput mode
#每次讀取一行
for f in open('test.txt'):
    print(f, end='')


