# 编写一个函数，利用欧几里得算法（脑补链接）求最大公约数，例如gcd(x, y)返回值为参数x和参数y的最大公约数

def gcd(x, y):
    # A, B = (x, y) if (x > y) else (y, x)
    # while True:
    #     tmp = A % B
    #     A = B
    #     B = tmp
    #     if (A % B == 0):
    #         print("最大公約數={0}".format(B))
    #         break
    while y:
        x, y = y, x % y

    print("最大公約數={0}".format(x))


gcd(123456, 7890)
