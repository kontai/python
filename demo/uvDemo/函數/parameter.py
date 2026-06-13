def foo(a, b, c):

    print(a, b, c)


def foo2(name, age: int = 18, *arg):

    print(name, age, arg)


if __name__ == "__main__":
    # foo(1, 2, 3)

    foo(*(1, 2, 3))
    # 將字典轉成參數,鍵必須和參數一樣
    d1 = {"a": 1, "b": 2, "c": 3}
    foo(**d1)
