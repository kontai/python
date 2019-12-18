#  Copyright (c) 2019.
#  classＭethod.py
#

class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


class SecondClass(FirstClass):
    def display(self):
        print("Current data is %s" % self.data)


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    # 重載'+'
    def __add__(self, other):
        return ThirdClass(self.data + other)

    # 重載'str'
    def __str__(self):
        return '[ThirdClass: %s]' % self.data

    # 重載'*'
    def mul(self, other):
        self.data *= other


if __name__ == '__main__':
    x = SecondClass()
    x.setdata("2nd class")
    x.display()  # 覆蓋FirstClass display方法

    a = ThirdClass('abc')
    a.display()  # 繼承SecondClass display菲奧法
    print(a)  # __str__被調用

    b = a + 'xyz'  # __add__被調用
    b.display()
    print(b)  # __str__被調用

    a.mul(3)
    print(a)
