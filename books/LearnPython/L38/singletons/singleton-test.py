# from singleton1 import singleton
# from singleton2 import singleton
# from singleton3 import singleton
from singleton4 import singleton

@singleton
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


@singleton
class Hack:
    def __init__(self, val):
        self.attr = val


sue = Person('Sue', 50, 20)
print(sue.name, sue.pay())

bob = Person('bob', 40, 30)
print(bob.name, bob.pay())

X = Hack(val=42)  # One Person, one Hack
Y = Hack(99)
print(X.attr, Y.attr)
