import sys
from 函數.迭代器與生成器.Mytimer import mytimer

reps = 10000
replist = range(reps)


def forloop():
    res = []
    for x in replist:
        res.append(abs(x))
    return res


def listComp():
    return [abs(x) for x in replist]


def mapCall():
    return list(map(abs, replist))


def genExpr():
    return list(abs(x) for x in replist)


def genFunc():
    def gen():
        for x in replist:
            yield abs(x)

    return list(gen())


m = dict()
print(sys.version)
for test in (forloop, listComp, mapCall, genExpr, genFunc):
    elapsed, result = mytimer.timer(test)
    m[test.__name__] = elapsed
    print("-" * 33)
    print("%-9s: %.5f => [%s...%s]  size=%d" % (test.__name__, elapsed, result[0], result[-1], len(result)))
a = sorted(m, key=lambda x: m[x])
elapsed, result = mytimer.timer(sorted, m, key=lambda x: m[x])
print("%-9s: %.5f => [%s...%s]  size=%d" % ("sort list", elapsed, result[0], result[-1], len(result)))

# print("*"*30)
# for x in a:
#     print("%10s %10.5f"%(x,m[x]))
