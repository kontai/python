from collections import Iterable

i = 0
sum = 0

dict_c = {"wang": 65, "chen": 33, "li": 49}
for k, v in dict_c.items():
    print("k=", k, "v=", v)
    sum += v
    i += 1
print("sum=", sum, "avg=", sum / i)

print(isinstance(dict_c, Iterable))
print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))
