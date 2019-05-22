# 请用已学过的知识编写程序，找出小甲鱼藏在下边这个长字符串中的密码，密码的埋藏点符合以下规律：
#   a) 每位密码为单个小写字母
#   b) 每位密码的左右两边均有且只有三个大写字母

string_file = open("L20-string2.txt", "r")
string = string_file.read()
lenth = len(string)
answer=""
for i in range(lenth):
    if (string[i].islower()):
        tmp = string[i - 3:i] + string[i + 1:i + 4]
        if tmp.isupper() and tmp.isalpha() and len(tmp)==6:
            answer+=string[i]

print(answer)
#print(string[i],sep=' ')
