# -*- coding=utf-8 -*-
'''
 24、实现一个整数加法计算器：
 如：
 content=input('请输入内容：')
 #
 如：5+9或5+9或5+9
cal=input(">>>")
value="5+9"
v1,v2=value.sp;it('+')

v1=int(v1)
v2=int(v2)
print(v1+v2)
# cal=cal.split(' ')
# print(cal)
# sum=int(cal[0])
# plus='+'
# tmp=0
# for i in cal[1:]:
#     if(i.isdecimal() and tmp==1):
#         sum+=int(i)
#     if(i=='+'):
#         tmp=1
#         continue
#print(sum)
'''

'''
25.计算用户输入的内容中有几个十进制小数？几个字母？
content=input(">>>")
num=0
alpha=0
for i in content:
    if(i.isdecimal()):
        num+=1
    elif(i.isalpha()):
        alpha+=1
print("num = ",num,",alpha = ",alpha)
'''
'''
制作表格
循环提示用户输入：用户名、密码、邮箱
（要求用户输入的长度不超过20 个字符，如果超过则只有前20 个字符有效）
如果用户输入
q 或Q
表示不再继续输入，将用户输入的内容以表格形式大隐
'''
template = "{0}\t{1}\t{2}\n"
s = ""
while True:
    v1 = input(">=")
    v2 = input(">>")
    v3 = input(">>>")
    s += template.format(v1, v2, v3)
    if (v1 + v2 + v3 == 'q'):
        break
print(s.expandtabs(20))
print(s.rstrip('b'))
