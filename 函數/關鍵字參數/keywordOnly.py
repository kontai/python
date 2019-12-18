# 如須指定參數只能用關鍵字傳遞，該參數要在*號後面(在**前面,如果有的話)

def kwonly(a, *b, c):
    print(a, b, c)


kwonly(1, 2, c=3)
kwonly(1, c=3)


# kwonly(1, 2, 3)   必須只用關鍵字


def kwonly2(a, *, c):
    print(a, c)


kwonly2(1, c=3)


def f(a, *b, c=6, **d): print(a, b, c, d)


f(1, *(2, 3), **dict(x=4, y=5))
f(1, *(2, 3), **dict(x=4, y=5), c=7)
