import re

#  元字符之字符集［］
ret = re.findall('a[bc]d', 'acd')
print(ret)  # ['acd']

ret = re.findall('[a-z]', 'acd')
print(ret)  # ['a', 'c', 'd']

ret = re.findall('[.*+]', 'a.cd+')
print(ret)  # ['.', '+']

# 在字符集里有功能的符号: - ^ \

ret = re.findall('[1-9]', '45dha3')
print(ret)  # ['4', '5', '3']

ret = re.findall('[^ab]', '45bdha3')
print(ret)  # ['4', '5', 'd', 'h', '3']

ret = re.findall('[\d]', '45bdha3')
print(ret)  # ['4', '5', '3']
