#!python

#1-100

import sys
sys.setrecursionlimit(10002)
def foo(L):
    sum = 0
    if L>0:
        sum+=L+foo(L-1)
    else:
        return 0
    return sum
print(foo(10))
