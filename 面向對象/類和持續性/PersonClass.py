#  Copyright (c) 2019.
#  Person.py (final)
#
from 面向對象.類和持續性.classtools import AttrDisplay


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


class Manager(Person):
    """
    A customized Person with special requirements
    """

    def __init__(self, name, pay=0):
        # super().__init__(name, 'mgr', pay)
        Person.__init__(self, name, 'mgr', pay)

    # 重寫Person中giveRaise方法

    def giveRaise(self, percent, bonus=.10):
        # self.pay = int(self.pay * (1 + percent + bonus))  #未達到真正擴展功能(Person公式更改,此處也跟著需要更改)
        Person.giveRaise(self, percent + bonus)

    def __getattr__(self, item):  # 如果 item 被访问，同时它不存在的时候，此方法被调用
        # return getattr(self.person,item)
        print("You use getattr")


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    # print(sue)
    # print(bob.lastName(), sue.lastName())
    # sue.giveRaise(.1)
    # print(sue)
    tom = Manager("Tom Jones", 500000)
    # tom.giveRaise(.10)
    # print(tom.lastName())
    # print(tom)

    tom.uu = 3  # 調用__getattr__
    print(tom.uu)
