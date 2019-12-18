#  Copyright (c) 2019.
#  fun.py
#
import types
from imp import reload


def read_fun(*args):
    print(type(args))
    for attr in args:
        if type(attr) == types.ModuleType:
            for obj in attr.__dict__.values():
                print('-' * 20)
                print(obj)
            read_fun(attr)


if __name__ == "__main__":
    import a

    read_fun(a)
