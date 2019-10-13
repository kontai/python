#  Copyright (c) 2019.
#  storeDB.py
#

from 面向對象.類和持續性.PersonClass import Person, Manager

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager("Tom Jones", 500000)

import shelve

# db = shelve.open('persondb')
with shelve.open('persondb') as db:
    print(type(db))
    for obj in (bob, sue, tom):
        db[obj.name] = obj
    # db.close()
