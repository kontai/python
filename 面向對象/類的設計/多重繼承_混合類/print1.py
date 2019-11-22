#  Copyright (c) 2019.
#  print1.py
#

from 面向對象.類的設計.多重繼承_混合類.lister import ListerInstance


class Spam(ListerInstance):
    def __init__(self):
        self.data1 = "food"


x = Spam()
print(x)
# 嘗試在console打印
x
