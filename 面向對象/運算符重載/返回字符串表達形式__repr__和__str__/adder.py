#  Copyright (c) 2019.
#  adder.py
#
"""
如果定義了__repr__，當類的實例打印或轉換成字符串時，_repr__(或__str__)就會自動調用。
"""


# Original
class adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other


x = adder()
print(x)


# with repr
class addrepr(adder):
    def __repr__(self):
        return "adderpr(%s)" % self.data


x = addrepr(2)
x + 1
print(x)
print(str(x), repr(x))


# with str
class addstr(adder):
    def __str__(self):
        return '[Value: %s]' % self.data


x = addstr(3)
x + 1
print(x)  # 在交互模式: >>x 會使用repr(x)顯示原始編碼,>>print(x)會調用str(x)
print(str(x), repr(x))


# with Both
# class addboth(addrepr,addstr):pass
class addboth(adder):
    def __str__(self):
        return '[Value: %s]' % self.data

    def __repr__(self):
        return 'addboth(%s)' % self.data


x = addboth(4)
x + 1
print(x)
print(str(x), repr(x))
