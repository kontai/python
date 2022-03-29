class common_cls:
    def __init__(self):
        pass


    def __set__(self, instance, value):
        if not isinstance(value, str):
            print('not string!')
            raise TypeError('類型錯誤 not str')
        else:
            instance.__dict__[value] = value
        print('callled __set__ function')


    def __get__(self, name, age):
        print('callled __get__ function ')


    def __del__(self):
        print('called __del__ funcgion')

class Dog:
    name = common_cls()
    age = common_cls()


    def __init__(self, name, age):
        self.name = name
        self.age = age

b = Dog('jj', 22)
print(b.__dict__)
