def func_with_fallback(func):
    def inn1func(*arg, **kargs):
        results = func(*arg, **kargs)
        print("The Function name:", func.__name__)
        print("Augument:", arg)
        print("result:", results)
        return results

    return inn1func

def func_another_test(func):
    def inn2func(*arg, **kargs):
        results = func(*arg, **kargs)
        return results * results

    return inn2func

@func_another_test
@func_with_fallback
@func_with_fallback
def add_int(a, b):
    return a + b

if __name__ == '__main__':
    # add2number = func_with_fallback(add_int)
    # print(add2number(2, 3))
    print(add_int(2, 3))

