def Init(**kwarg):
    def Wrapper(obj):
        for k,v in kwarg.items():
            # obj.k=v
            # print('--->',k,v)
            setattr(obj,k,Foo(k,v))
        return obj
    return Wrapper


class Foo:
    def __init__(self, value, Itype):
        self.value = value
        self.Itype = Itype

    def __set__(self, instance, value):
        print("(===>calling __set__)", instance, value)
        if isinstance(value, self.Itype):
            instance.__dict__[self.value] = value
        else:
            raise TypeError;
            print("類型錯誤!")
        return instance

    def __get__(self, instance, owner):
        print("(--->calling __get__)")
        return True

    def __delete__(self, instance):
        print("XXXXX __delete__")
        instance.__dict__.pop('name')


@Init(name=str, gender=str)
class Petch:
    # name = Foo("name", str)
    # gender = Foo("gender", str)

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


I = Petch("kontai", "male")
print(I.name)

print(I.__dict__)
I.name = "ABC"
print(I.__dict__)
print(dir(I))
del I.name
print(I.__dict__)


