#  Copyright (c) 2019.
#  SkipIter.py
#
"""
相同數據的多個迭代
"""


class SkipIterator:
    def __init__(self, wrapped):  # 每次調用都會產生新迭代對象
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item


class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)  # 定義新的狀態對象


if __name__ == '__main__':
    alpha = 'abcdef'
    X = SkipObject(alpha)
    for i in X:
        for j in X:
            print(i + j, end=' ')

    I = iter(X)
    print('\n' + next(I), next(I), next(I))

    # 分片也可以達到同樣效果，但分片是一次性放進內存，較消耗資源
    A = alpha[::2]

    print(A)
    for x in A:
        for y in A:
            print(x + y, end=' ')
