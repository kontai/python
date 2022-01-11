a = "abc,def"
b = tuple(a.split(','))
print(b)

str1 = '&'.join(b)
print(b, str1)

# 利用逗點創建tuple
c = a, b
print(c)

d = "anc", "def"
print(d, type(d))

list1=[["abc","kontai","1"],"de"]
list2=["abc","def","ghi"]
# print(1 in list1[0])
joined='-'.join(list1[0])
print(joined)
