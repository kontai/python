class anotherDog(object):
    __name = 'aFu'

    @classmethod
    def clsMehod(cls, name):
        cls.__name = name
        return cls.__name

    def fakeClsMethod(self, name):
        self.__name = name
        return self.__name


if __name__ == '__main__':
    '''
    print(anotherDog.name)
    myDog = anotherDog()
    print(myDog.name)
    anotherDog.name = 'jason'
    print(anotherDog.name)
    print(myDog.name)
    hisDog = anotherDog()
    print(hisDog.name)
    '''
    c1 = anotherDog()
    print(c1.clsMehod('tai'))
    print(c1.fakeClsMethod('tai?'))
