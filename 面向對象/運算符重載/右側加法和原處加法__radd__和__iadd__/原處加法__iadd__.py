#  Copyright (c) 2019.
#  原處加法__iadd__.py
#

"""
使用__iadd__和__add__實現+=原處加法,如果缺少__iadd__,則使用__add__
由於是原處加法,返回是self(實例本身)
"""


class Number:
    def __init__(self, val):
        self.val = val

    def __iadd__(self, other):  # __iadd__explicit: x+=y
        print("iadd %s" % other)
        self.val += other  # Usually returns self
        return self

    def __add__(self, other):  # __add__fallback: x=(x+y)
        print("add %s" % other)
        return Number(self.val + other)  # Propagates class type


x = Number(5)
x += 1
x += 1
print(x.val)
