#  Copyright (c) 2019.
#  life.py
#

"""
每當實例產生，就會調用__init__構造函數。每當實例空間被收回時（在垃圾收集時）
他的對立面__del__，也就是析構函數（destructor method)，就會自動執行。
"""


class Life:
    def __init__(self, name="unknown"):
        print("Hello", name)
        self.name = name

    def __del__(self):
        print("Goodbye", self.name)


brian = Life("Brian")

# 當brain賦值為字符串時，會失去Life實例的最後一個引用。因此觸發析構函數。
# 在Python中，析構函數並不常使用
brian = "loretta"
