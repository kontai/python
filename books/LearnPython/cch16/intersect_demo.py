X = 3


def foo():
    global X
    a = 6
    X = 4

    def inner():
        # nonlocal a
        a = 7

    inner()
    print(a)


foo()
print('x=', X)
