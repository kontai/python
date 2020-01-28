class MyType(type):
    def __init__(self,a,b,c):
        print('元類的構造函數執行')
    def __call__(self, *args, **kwargs):
        obj=object.__new__(self)
        self.__init__(obj,*args,**kwargs)
        return obj
class Foo(metaclass=MyType):
    def __init__(self,name):
        self.name=name
f1=Foo('alex')