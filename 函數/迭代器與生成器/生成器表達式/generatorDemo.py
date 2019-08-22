X=[x**2 for x in range(4)]
print(X)

#返回生成器對象，而非在內存中構建結果。
Y=(x**2 for x in range(4))
print(Y)
# print(list(Y))
# print(next(Y))
# print(next(Y))
# print(next(Y))
for num in Y:
    print("%s , %s"%(num,num/2.0))
