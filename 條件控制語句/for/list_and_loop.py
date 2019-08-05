import random

a = list()
c = [x * y for x in range(1, 100000) for y in range(1,19999)]
# b = [x.append(y) for x in a for y in random.randint(1, 1000)]
print(c)
print(len(c))