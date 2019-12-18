def fetcher(obj, index):
    return obj[index]


def catcher():
    try:
        fetcher(x, 4)
    except IndexError:
        print("got exception")
    # finally語句不管異常是否發生，都會進入執行
    else:
        print("aa")
    finally:
        print("after fetch")

# 如果發生異常，此語句將不會執行
print("continuing")

x = "spam"
print(fetcher(x, 3))
catcher()
