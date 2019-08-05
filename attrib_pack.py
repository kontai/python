#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Washer:
    def __init__(self, water=10, scour=2):
        self._water = water
        self._scour = scour

    @property
    def water(self):
        return self._water

    @water.setter
    def water(self, water):
        if 0 < water < 300:
            self._water = water
        else:
            print("Failure")

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
    print(w.water)
    w.water = 200
    print(w.water)
