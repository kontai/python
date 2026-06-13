import re

str='hell 1world2'

res=re.findall(r'\d+',str)
print(res)

#將world匹配出來(移除數字)
words=re.search(r'\d(?P<name>(\w+))\d',str)
print(words.group('name'))
# res=re.findall(r'(?P<name>\d+(\w+)\d+)',str)
# print(res)
