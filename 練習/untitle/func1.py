def outer(a, b):
    def inner(c, d):
        return c + d

    return inner(a, b)

def outer2(a, *b):
    def inner():
        l = list((a))
        print(l)
        return a, b

    return inner

if __name__ == '__main__':
    l=list()
    l+=((2,3,4),)
    l+=(2,3,4)
    print(l)
# run_test=outer
# run_test2,run_test3=outer2(3,[2,3,4])
# print(type(run_test2),type(run_test3))
# print(run_test2(),run_test3())

# print(run_test(2, 3))
