#  Copyright (c) 2019.
#  exp.py
#

class Spam:
    def doit(self, message):
        print(message)


object1 = Spam()
object1.doit("hello world")

# 綁定方法
x = object1.doit
x("hello world")  # <bound method Spam.doit of <__main__.Spam object at 0x047E4F70>>
print(x)

# 無綁定
t = Spam.doit
t(object1, "howdy")  # 必須傳入實例作為最左側參數。


# 擴展
class Eggs:
    def m1(self, n):
        print(n)

    def m2(self):
        x = self.m1
        x(43)


Eggs().m2()
