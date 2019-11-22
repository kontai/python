#  Copyright (c) 2019.
#  setwrapper.py
#


class Set:
    def __init__(self, value=[]):  #构造函数
        self.data = []
        self.concat(value)

    def intersect(self, other):  #求交集
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)  #返回一个新的Set

    def union(self, other):  #求并集
        res = self.data[:]  #复制self.data
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def __len__(self):  # len(self)
        return len(self.data)

    def __getitem__(self, key):  # self[i]
        return self.data[key]

    def __and__(self, other):  # self & other
        return self.intersect(other)

    def __or__(self, other):  # self | other
        return self.union(other)

    def __repr__(self):  # print
        return 'Set:' + repr(self.data)


if __name__ == '__main__':  #测试用例
    x = Set([1, 3, 5, 7])
    print(x.union(Set([1, 4, 7])))
    print(x | Set([1, 4, 6]))
    print(x[2])
    print(x[2:4])
