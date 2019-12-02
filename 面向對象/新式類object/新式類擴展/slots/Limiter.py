#  Copyright (c) 2019.
#  Limiter.py
#

class limiter(object):
    __slots__ = ['age', "name", "job"]


x = limiter()
# print(x.age)    # Must assign before use
x.age = 40
print(x.age)
# x.ape=1000  # Illegal:not in__slots__
