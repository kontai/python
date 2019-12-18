#  Copyright (c) 2019.
#  In.py
#
"""
優先級
__contains__ > __iter__ > __getitem__

__contains__方法應該把成員關係定義成為一個映射應用鍵（並且可以使用快速查找），以及用於序列的搜索。
"""


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, item):
        print("get[%s]" % item, end=' ')
        return self.data[item]

    # def __iter__(self):
    #     print("iter=> ", end=' ')
    #     self.ix = 0
    #     return self

    def __next__(self):
        print("next: ", end=' ')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    # def __contains__(self, x):
    #     print("contains: ", end=' ')
    #     return x in self.data


if __name__ == '__main__':
    """
    依照順序註釋__contaons__．__iter__．觀察輸出結果。
    """
    X = Iters([1, 2, 3, 4, 5])
    print(3 in X)
    for i in X:
        print(i, end=" | ")
    print()
    print([i ** 2 for i in X])
    print(list(map(bin, X)))

    I = iter(X)
    while True:
        try:
            print(next(I), end=" @ ")
        except StopIteration:
            break
    print()
    print(X[0])
    print(X[1])
