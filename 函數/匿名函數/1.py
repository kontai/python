i=1
def foo():
    global i
    i+=1
    print('from foo')
    return foo
h=foo()
print(i)
h()
print(i)
