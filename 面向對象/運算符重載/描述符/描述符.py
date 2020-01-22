class Foo:
    '''
     描述符是什么:描述符本质就是一个新式类,在这个新式类中,至少实现了__get__(),__set__(),__delete__()中的一个,这也被称为描述符协议
    __get__():调用一个属性时,触发
    __set__():为一个属性赋值时,触发
    __delete__():采用del删除属性时,触发

    描述符是干什么的:描述符的作用是用来代理另外一个类的属性的(必须把描述符定义成这个类的类属性，不能定义到构造函数中)

     描述符分两种
        一 数据描述符:至少实现了__get__()和__set__()
        二 非数据描述符:没有实现__set__()

    注意事项:
        一 描述符本身应该定义成新式类,被代理的类也应该是新式类
        二 必须把描述符定义成这个类的类属性，不能为定义到构造函数中
        三 要严格遵循该优先级,优先级由高到底分别是
            1.类属性
            2.数据描述符
            3.实例属性
            4.非数据描述符
            5.找不到的属性触发__getattr__()
    '''
    def __get__(self, instance, owner):
        print('===>get方法')
    def __set__(self, instance, value):
        print('===>set方法',instance,value)
        instance.__dict__['x']=value #b1.__dict__
    def __delete__(self, instance):
        print('===>delete方法')


class Bar:
    x=Foo()
    # x被賦值於被描述的類,成了被描述的對象
    # 任何對x的set,get,delete都會觸發描述符
    def __init__(self,n):
        self.x=n #b1.x=10
b1=Bar(10)
print(b1.__dict__)
b1.x=11111111111111111
print(b1.__dict__)

b1.y=11111111111111111111111111111111111111
print(b1.__dict__)
# print(Bar.__dict__)
#在何时？
# b1=Bar()
# b1.x
#
# b1.x=1
#
# del b1.x

# print(b1.x)
#
# b1.x=1
# print(b1.__dict__)
#
# del b1.x

