#  Copyright (c) 2019.
#  嵌套中的對象打印.py
#

class Printer:
    def __init__(self, value):
        self.val = value

    def __str__(self):
        return str(self.val)


objs = [Printer(2), Printer(3)]
for x in objs: print(x)
print(objs)  # __str__只有當對象出現在一個打印操作頂層的時候才調用


# with repr
class PrinterRepr:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)


objs = [PrinterRepr(2), PrinterRepr(3)]
for x in objs: print(x)
print(objs)
