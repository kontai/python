#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Washer:
    def __init__(self, water=10, scour=2):
        self.water = water
        self.scour = scour

    def set_scour(self, scour):
        self.scour = scour

    def add_water(self):
        print('Add water:', self.water)

    def add_scour(self):
        print("Add scour:", self.scour)

    def start_wash(self):
        self.add_water()
        self.add_scour()
        print("Start wash...")


if __name__ == "__main__":
    w = Washer()
    # w.water=100
    # w.scour=10
    w.start_wash()
