# 编写一个程序，求 100~999 之间的所有水仙花数。
len = 0
for i in range(100, 999):
    if (i // 100) ** 3 + (i // 10 % 10) ** 3 + (i % 10) ** 3 == i:
        print(i, end='\t')
        len += 1
print('\nlen=', len)
