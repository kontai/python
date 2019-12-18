#  Copyright (c) 2019.
#  manynames.py
#
X = 11


def f():
    print(X)


def g():
    X = 22
    print(X)


class C:
    X = 33

    def m(self):
        X = 44
        self.X = 55


if __name__ == "__main__":
    print(X)  # 11:module (a.k.a manynames.X outside file)
    f()  # 11:global
    g()  # 22:local
    print(X)  # 11:module name unchanged

    obj = C()  # Make instance
    print(obj.X)  # 33:class name inherited by instance

    obj.m()  # Attach attribute name X to instance now
    print(obj.X)  # 55:instance
    print(C.X)  # 33:class(a.k.a. obj.X if no X in instance)

    # print(C.m.X)  #FAILS: only visible in method
    # print(g.X)    #FAILS: only visible in function
