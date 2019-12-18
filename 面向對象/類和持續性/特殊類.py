#  Copyright (c) 2019.
#  特殊類.py
#

from 面向對象.類和持續性.PersonClass import Person

bob = Person('Bob Smith')
print(bob)

print(bob.__class__)
print(bob.__class__.__name__)
print(list(bob.__dict__.keys()))
for key in bob.__dict__:
    print(key, "==>", bob.__dict__[key])

print(list(bob.__dict__.keys()))
print(dir(bob))
