#  Copyright (c) 2019.
#  類傳播避免嵌套.py
#

class Commuter:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if isinstance(other, Commuter): other = other.val
        return Commuter(self.val + other)

    def __radd__(self, other):
        return Commuter(other + self.val)

    def __str__(self):
        return "<Commuter: %s>" % self.val


if __name__ == '__main__':
    x = Commuter(88)
    y = Commuter(99)
    print(x + 10)
    print(10 + y)
    z = x + y
    print(z)
    print(z + 10)
    print(z + z)
