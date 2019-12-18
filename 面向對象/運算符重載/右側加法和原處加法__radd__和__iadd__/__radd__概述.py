#  Copyright (c) 2019.
#  Computer.py
#
"""
__add__方法並不支持+運算符右側使用實例對象。
要實現支持可互換的運算符，可以一併編寫__radd__方法。
只有當+右側的對象是類實例，而左邊對象不是類實例時,Python才會調用__radd__
在其他所有情況下，則由左側對象調用__add__方法。
"""


class Commuter:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print("add", self.val, other)
        return self.val + other

    def __radd__(self, other):
        print("radd", self.val, other)
        return self.val + other


x = Commuter(88)
y = Commuter(99)
print(x + 1)
print(1 + y)

print(x + y)
