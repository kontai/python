#  Copyright (c) 2019.
#  otherfile.py
#

from 作用域 import manynames
from 作用域.manynames import *

X = 66  # 66:the global here
print(X)  # 11:global become attributes after imports
print(manynames.X)  # 11:manynames's X.not the one here!
manynames.f()  # 22:local in other file's function
manynames.g()

print(manynames.C.X)  # 33:attribute of class in other module
I = manynames.C()
print(I.X)  # 33:still from class here
I.m()
print(I.X)  # 55: now from instance!
