<<<<<<< HEAD
i=1
def foo():
    global i
    i+=1
    print('from foo')
    return foo
h=foo()
=======
i = 1


def foo():
    global i
    i += 1
    print('from foo')
    return foo


h = foo()
>>>>>>> 1218
print(i)
h()
print(i)
