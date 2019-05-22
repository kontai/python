from collections import Iterable


def var_sum(*number):
    sum = 0
    for x in number:
        sum += x * x
    return sum


def dic_in(name="", age=0, **dic_num):
    #print('name', name, "age", age, "other", dic_num)
    print((dic_num.items))


print(var_sum(12, 3))

list_a = [3, 4, 5]
print(var_sum(*list_a))

tuple_b = (3, 4, 5, 6)
print(var_sum(*tuple_b))

dict_c = {"wang": 65, "chen": 33, "li": 49}
dic_in(**dict_c)
