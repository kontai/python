#  Copyright (c) 2019.
#  setsubclass.py
#

### file: setsubclass.py

class Set(list):
    def __init__(self, value=[]):  # Constructor
        list.__init__(self, [])  # Customizes list
        # super(Set, self).__init__([])
        # print("Test in __init__ -> ",self)
        self.concat(value)  # Copies mutable defaults

    def intersect(self, other):  # other is any sequence
        res = []  # self is the subject
        for x in self:
            if x in other:  # Pick common items
                res.append(x)
        return Set(res)  # Return a new Set

    def union(self, other):  # other is any sequence
        res = Set(self)  # Copy me and my list
        res.concat(other)
        return res

    def concat(self, value):  # value: list, Set . . .
        for x in value:  # Removes duplicates
            if not x in self:
                self.append(x)

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return 'Set:' + list.__repr__(self)


if __name__ == '__main__':
    x = Set([1, 3, 5, 7])
    y = Set([2, 1, 4, 5, 6])
    print(x, y, len(x))
    print(id(x), id(y))
    print(x.intersect(y), y.union(x))
    print(x & y, x | y)
    x.reverse();
    print(x)
    x
