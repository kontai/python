#  Copyright (c) 2019.
#  1-Numbers.py
#

class Number:
    def __init__(self, base):
        self.base = base

    def double(self):
        return self.base * 2

    def triple(self):
        return self.base * 3


x = Number(2)
y = Number(3)
z = Number(4)

print(x.double())
print()

acts = [x.double, y.double, z.double]
for act in acts:
    print(act())

######################
# 綁定方法對象擁有自己的內省性息
######################

bound = x.double
print(bound.__self__, bound.__func__)
print(bound.__self__.base)
print(bound())
