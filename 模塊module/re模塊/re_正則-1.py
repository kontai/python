import re

# 元字符之. ^ $ * + ? { }
ret = re.findall('a..in', 'helloalvin')
print(ret)  # ['alvin']

ret = re.findall('^a...n', 'alvinhelloawwwn')
print(ret)  # ['alvin']

ret = re.findall('a...n$', 'alvinhelloawwwn')
print(ret)  # ['awwwn']

ret = re.findall('a...n$', 'alvinhelloawwwn')
print(ret)  # ['awwwn']

ret = re.findall('abc*', 'abcccc')  # 贪婪匹配[0,+oo]
print(ret)  # ['abcccc']

ret = re.findall('abc+', 'abccc')  # [1,+oo]
print(ret)  # ['abccc']

ret = re.findall('abc?', 'abccc')  # [0,1]
print(ret)  # ['abc']

ret = re.findall('abc{1,4}', 'abccc')
print(ret)  # ['abccc'] 贪婪匹配

# 注意：前面的 *, +,?等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配
ret = re.findall('abc*?', 'abcccccc')
print(ret)  # ['ab']
ret = re.findall('abc+?', 'abcccccc')
print(ret)  # ['ab']

#12+(34*6+2-5*(2-1))  ----   提出最裡面的括號(2-1)
#
#
#
#
#
#
#
#
#
#
#
re.findall("\([^()]*\)","12+(34*6+2-5*(2-1))")
