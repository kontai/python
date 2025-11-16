import time

reps = 1000
repslist = range(reps)


def timer(func, *pargs, **kargs):
    start = time.clock()
    t = 0
    for i in repslist:
        ret = func(*pargs, **kargs)
        t += 1
    print(t)
    elapsed = time.clock() - start
    return (elapsed, ret)
