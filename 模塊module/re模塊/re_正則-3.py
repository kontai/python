import re

# 元字符之转义符 \
#  \
# 反斜杠后边跟元字符去除特殊功能, 比如\.
# 反斜杠后边跟普通字符实现特殊功能, 比如\d
#
# \d
# 匹配任何十进制数；它相当于类[0 - 9]。
# \D
# 匹配任何非数字字符；它相当于类[ ^ 0 - 9]。
# \s
# 匹配任何空白字符；它相当于类[ \t\n\r\f\v]。
# \S
# 匹配任何非空白字符；它相当于类[ ^ \t\n\r\f\v]。
# \w
# 匹配任何字母数字字符；它相当于类[a - zA - Z0 - 9_]。
# \W
# 匹配任何非字母数字字符；它相当于类[ ^ a - zA - Z0 - 9_]
# \b
# 匹配一个特殊字符边界，比如空格 ， & ，＃等

ret = re.findall('I\b', 'I am LIST')
print(ret)  # []
ret = re.findall(r'I\b', 'I am LIST')
print(ret)  # ['I']

# -----------------------------eg1:
# ret = re.findall('c\l', 'abc\le')
print(ret)  # []
# ret = re.findall('c\\l', 'abc\le')
print(ret)  # []
ret = re.findall('c\\\\l', 'abc\le')
print(ret)  # ['c\\l']
ret = re.findall(r'c\\l', 'abc\le')
print(ret)  # ['c\\l']

# -----------------------------eg2:
# 之所以选择\b是因为\b在ASCII表中是有意义的
m = re.findall('\bblow', 'blow')
print(m)
m = re.findall(r'\bblow', 'blow')
print(m)
