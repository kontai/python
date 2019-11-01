#  Copyright (c) 2019.
#  pizzashop.py
#
"""
OOP與組合
"""
from 面向對象.類的設計.繼承與組合.employee import PizzaRobot, Server


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, "oders form", server)

    def pay(self, server):
        print(self.name, "pays for item to", server)


class Oven:
    def bake(self):
        print("over bakes")


class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = PizzaRobot("Bob")
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


if __name__ == '__main__':
    scene = PizzaShop()
    scene.order("Homer")
    print("...")
    scene.order("Shaggy")
