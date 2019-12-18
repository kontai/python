# 编写一个将十进制转换为二进制的函数，要求采用“除2取余”（脑补链接）的方式，结果与调用bin()一样返回字符串形式。
def dtob(dec):
    tmp = []
    while (dec):
        bin = dec % 2
        dec //= 2
        tmp.append(bin)

    bb = ''
    while tmp:
        bb += (str)(tmp.pop())
        # print(tmp.pop(),end='')
    print(type(bb), bb)


dtob(10)
