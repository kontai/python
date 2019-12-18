# 默認參數是在def語句運行時評估並保守的，而不是再這個函數調用時。
# 從內部來講。python會將每一個默認參數保存成一個對象，附加再這個函數本身。
# 不會每次調用時都會得到新的列表

def saver(x=[]):
    x.append(1)
    print(x)


print(saver([2]))
saver()
saver()
saver()
saver([2, 3])
saver()


def saver2(x=None):
    # x=x or []
    #  如果參數為空列表,即[] or [],將會在此使用新的空列表,而非使用調用函數時所傳進的空列表
    if x is None:
        x = []
    x.append(1)
    print(x)


saver2()
saver2([33, 44])
saver2([])
