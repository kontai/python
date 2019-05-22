#请用已学过的知识编写程序，统计下边这个长字符串中各个字符出现的次数并找到小甲鱼送给大家的一句话
string_file=open("L20-string1.txt","r")
string=string_file.read()
def countSting(a):
    lis = []
    loc = 0
    for i in range(len(a)):
        if a[i] not in lis:
            lis.append(a[i])
            lis.append(1)
        else:
            b = lis.index(a[i])
            lis[b + 1] += 1
    lenth = len(lis)
    for j in range(0, lenth, 2):
        print("%s\t:%d" % (lis[j], lis[j + 1]))


countSting(string)
