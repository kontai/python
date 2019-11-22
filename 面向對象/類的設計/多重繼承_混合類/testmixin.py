#  Copyright (c) 2019.
#  testmixin.py
#

# from 面向對象.類的設計.多重繼承_混合類.lister import *
# from 面向對象.類的設計.多重繼承_混合類.使用dir列出繼承的屬性.listerWithDir import *
from 面向對象.類的設計.多重繼承_混合類.列出類樹中每個對象的屬性.listerTree import *


class Super:
    def __init__(self):
        self.data1 = "spam"

    def ham(self):
        pass


# class Sub(Super,ListerInstance):
# class Sub(Super, ListInherited):
class Sub(Super, ListTrees):
    def __init__(self):
        Super.__init__(self)
        self.data2 = "eggs"
        self.data3 = 42

    def spam(self):
        pass


if __name__ == "__main__":
    X = Sub()
    print(X)
