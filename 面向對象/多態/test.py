# _*_ coding=utf-8 _*_

class Base:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)


a = Base('kontai')
a.get_name()
print(dir(a))
