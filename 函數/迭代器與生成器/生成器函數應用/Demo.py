# 函數在每次循環都會產生一個值，之後將其返回給他的調用者
# 1
def gensquares(N):
    for i in range(N):
        yield i ** 2


for i in gensquares(5):
    print(i, end=' : ')
print('\n')


# 2
def buildsquares(n):
    res = []
    for i in range(n): res.append(i ** 2)
    return res


for x in buildsquares(5): print(x, end=' : ')
print('\n')

# 3
for n in [i ** 2 for i in range(5)]:
    print(n, end=' : ')
print('\n')

# 4
for n in map((lambda x: x ** 2), range(5)):
    print(n, end=' : ')
