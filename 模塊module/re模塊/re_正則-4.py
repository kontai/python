import re

# 元字符之分组()
m = re.findall(r'(ad)+', 'add')
print(m)

ret = re.search('(?P<id>\d{2})/(?P<name>\w{3})', '23/com')
print(ret.group())  # 23/com
print(ret.group('id'))  # 23

# 元字符之｜
ret = re.search('(ab)|\d', 'rabhdg8sd')
print(ret.group())  # ab
