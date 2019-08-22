# f被賦值一個lambda表達式創建的函數對象
f = lambda x, y, z: z + y + z
print(f(2, 3, 4))

# 默認參數也能在lambda中使用
x = (lambda a="fee", b="fie", c="foe": a + b + c)
print(x("wee"))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)


# 函數嵌套lambda
def knight():
    title = 'sir'
    action = (lambda x: title + ' ' + x)
    return action


act = knight()
print(act('robin'))

# list元素為lambda表達式
L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4,
     ]

for f in L:
    print(f(2), end=' ')
print('\n', L[0](3))

# dict & lambda
key = 'got'
res = {'already': (lambda: 2 + 2),
       'got': (lambda: 2 * 4),
       'one': (lambda: 2 ** 6)}
print(res[key]())
