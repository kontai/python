#  Copyright (c) 2019.
#  Person.py (final)
#
from 面向對象.類基本實現.classtools import AttrDisplay
from 面向對象.類基本實現.ManagerClass import Manager
class Person(AttrDisplay):
    """
    Create and process person records
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # def __str__(self):
    #     return '[Person: %s, %s]' % (self.name, self.pay)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.1)
    print(sue)
    tom=Manager("Tom Jones",500000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
