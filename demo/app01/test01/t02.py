def test():
    for i in range(4):
        yield i

t = test()

for i in t:
    print(i)

t1=(i for i in t)
# print(list(t1))