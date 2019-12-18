#  Copyright (c) 2019.
#  02-索引迭代.py
#
'''
__getitem__也可以是python中一種重載迭代的方式。
如果定義了這種方法，for循環每次循環是時都會調用__getitem__,並持續搭配有更高的偏移值。
任何會影響索引運算的內置或用戶定義的對象，同樣會影響迭代。
'''


class stepper:
    def __getitem__(self, i):
        return self.data[i]


X = stepper()
X.data = "Spam"
print(X[1])

for item in X:
    print(item, end=' ')
print("\n")
print('p' in X)
print(list(map(str.upper, X)))
(a, b, c, d) = X
print(a, c, d)
print(X)
