#  Copyright (c) 2019.
#  類外動態增加屬性及方法.py
#

class rec: pass


rec.name = 'Bob'
rec.age = 40
print(rec.name)

x = rec()
y = rec()
print(x.name, y.name)

x.name = "susan"
print(rec.name, x.name, y.name)


###########################動態增加方法##########################

def upperName(self):
    return self.name.upper()


def setName(self, name):
    self.name = name


print(upperName(x))

rec.method = upperName  # 為類型新增方法
print(x.method())
print(y.method())
print(rec.method(x))

from types import MethodType  # MethodType作用就是把类外面的方法绑定到类或者类的实例上面

x.set_name = MethodType(setName, x)
x.set_name('jojo')
print(x.name)


class Student(object): pass


s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print(s.name)


# 还可以尝试给实例绑定一个方法：

def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
