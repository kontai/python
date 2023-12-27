import sys, mytimer  # Import timer function

"""
timer(spam, 1, 2, a=3, b=4, _reps=1000) calls and times spam(1, 2, a=3) 
_reps times, and returns total time for all runs, with final result; 

best(spam, 1, 2, a=3, b=4, _reps=50) runs best-of-N timer to filter out 
any system load variation, and returns best time among _reps tests
"""
# import sys, mytimer3
import sys,mytimer3_forpy3x
reps = 10000
repslist = range(reps)


def forLoop():
    res = []
    for x in repslist:
        res.append(x + 10)
    return res


def listComp():
    return [x + 10 for x in repslist]


def mapCall():
    return list(map((lambda x: x + 10), repslist))  # list() in 3.0 only


def genExpr():
    return list(x + 10 for x in repslist)  # list() in 2.6 + 3.0


def genFunc():
    def gen():
        for x in repslist:
            yield x + 10

    return list(gen())


print(sys.version)
for tester in (mytimer3_forpy3x.timer, mytimer3_forpy3x.best):
    print('<%s>' % tester.__name__)
    for test in (forLoop, listComp, mapCall, genExpr, genFunc):
        elapsed, result = tester(test)
        print('-' * 35)
        print('%-9s: %.5f => [%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))
