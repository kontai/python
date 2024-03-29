import sys, mytimer  # Import timer function

reps = 10000
repslist = range(reps)  # Hoist range out in 2.6


def forLoop():
    res = []
    for x in repslist:
        res.append(x + 10)
    return res

def listComp():
    return [x + 10 for x in repslist]

def mapCall():
    return list(map((lambda x: x + 10), repslist))          # list() in 3.0 only

def genExpr():
    return list(x + 10 for x in repslist)                   # list() in 2.6 + 3.0

def genFunc():
    def gen():
        for x in repslist:
            yield x + 10
    return list(gen())

print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    elapsed, result = mytimer.timer(test)
    print('-' * 33)
    print('%-9s: %.5f => [%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))
