x = 2


def ch():
    global x
    x = 3


def ch2():
    import changes_global
    changes_global.x += 1


def ch3():
    pass
