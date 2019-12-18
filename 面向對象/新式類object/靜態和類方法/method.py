#  Copyright (c) 2019.
#  method.py
#

class Method:
    def imeth(self, x):  # Normal instance method: passed a self
        print(self, x)

    def smeth(x):  # Static: no instance passed
        print(x)

    def cmeth(cls, x):  # Class: gets class,not instance
        print(cls, x)

    smeth = staticmethod(smeth)  # Make smeth a statice method
    cmeth = classmethod(cmeth)  # Make cmeth a class method


obj = Method()  # Make an instance
obj.imeth(1)  # Normal method,call through instance
Method.imeth(obj, 2)  # Normal method,call through class

# 靜態方法調用時不需要實例參數。
Method.smeth(3)  # Static method call through class
obj.smeth(4)  # Static method:call through instance

# 類方法自動把類（而不是實例）傳入類方法第一個（最左側）參數中，不管他是通過一個實例或者一個類調用。
Method.cmeth(5)
obj.cmeth(6)
