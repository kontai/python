#  Copyright (c) 2019.
#  索引和分片 __getitem__和__setitem__.py
#

class Indexer:
    def __getitem__(self, item):
        return item ** 2


X = Indexer()
print(X[2])

for i in range(5):
    print(X[i], end=' ')

# 攔截分片
print("\n")
print("*" * 30)


class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, *index):
        for i in index:
            print('getitem:', i)
            return self.data[i]


X = Indexer()
print(X[0])
print(X[1])
print(X[-1])

print(X[slice(2, 4)])

print(X[1:])
print(X[2:4])
