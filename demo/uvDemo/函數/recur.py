def rec(num):
    if num == 0:
        print('init number must be > 0')
        return
    if num < 5:
        return num * rec(num + 1)
    return num


res = rec(1)
print(res)
