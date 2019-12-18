#  Copyright (c) 2019.
#  模擬實例屬性的私有性p1.py
#
class PrivaateExc(Exception): pass


class Privacy:
    def __setattr__(self, attrname, value):
        if attrname in self.privates:
            raise PrivaateExc(attrname, self)
        else:
            self.__dict__[attrname] = value


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ["name", "pay"]

    def __init__(self):
        self.__dict__["name"] = "Tom"


x = Test1()
y = Test2()
x.name = "Bob"
y.name = "Sue"
y.age = 30
x.age = 49
