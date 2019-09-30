import sys, time


def f(func, *args, _reps=1000, **kargs):
    # if sys.platform[:3] == "win":
    #     timetype = time.clock
    # else:
    #     timetype = time.time
    timetype = time.time
    start = timetype()
    for i in range(_reps):
        ret = func(*args, **kargs)
    elapsed = timetype() - start
    return (elapsed, ret)


def power(x, y): return x ** y


print(f(lambda *args: args[0] ** args[1], 2, 32, _reps=10000000))
