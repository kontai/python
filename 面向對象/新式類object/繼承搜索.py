#  Copyright (c) 2019.
#  繼承搜索.py
#

class A(object):
    attr = 1


class B(A): pass


class C(A):
    attr = 2


class D(B, C):
    # pass
    attr = A.attr


if __name__ == '__main__':
    I = D()
    print(I.attr)
