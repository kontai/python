# __*__coding:utf-8__*__
# class Foo(object):
#     """类三种方法语法形式"""

#     def instance_method(self):
#         print("是类{}的实例方法，只能被实例对象调用".format(Foo))

#     @staticmethod
#     def static_method():
#         print("是静态方法")

#     @classmethod
#     def class_method(cls):
#         print("是类方法")

# foo = Foo()
# foo.instance_method()
# foo.static_method()
# foo.class_method()
# print('----------------')
# Foo.static_method()
# Foo.class_method()

#####################################################

# clasos Book(object):
#    """类方法用在模拟java定义多个构造函数的情况"""
#     def __init__(self, title):
#         self.title = title

#     @classmethod
#     def create(cls, title):
#         book = cls(title=title)
#         return book


# book1 = Book("Python")
# book2 = Book.create("Python and django")
# print(book1.title)
# print(book2.title)

##################################################

