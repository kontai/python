#  Copyright (c) 2019.
#  ManagerClass.py
#

from 面向對象.類基本實現.PersonClass import Person

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

    def __getattr__(self, item):    #如果 item 被访问，同时它不存在的时候，此方法被调用
            # return getattr(self.person,item)
        print("You use getattr")

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)

    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.1)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    tom.uu=3      #調用__getattr__
    print(tom.uu)

    print(tom.lastName())
    print(tom)

    # print("---All three---")
    # for object in (bob, sue, tom):
    #     object.giveRaise(.10)
    #     print(object)

'''
    class Department:
        def __init__(self, *args):
            self.members = list(args)

        def addMember(self, person):
            self.members.append(person)

        def giveRises(self, percent):
            for person in self.members:
                person.giveRaise(percent)

        def showAll(self):
            for person in self.members:
                print(person)



    development = Department(bob, sue)
    development.addMember(tom)

    development.giveRises(.10)
    development.showAll()
'''
