'''
 Arhandle Arbitrarity nested sublists
[1, [2, [3, 4], 5], 6, [7, 8]]
'''


def sumtree(L, trace=False):
    total = 0
    for i in L:
        if not isinstance(i, list):
            total += i
            if trace:
                print(i, end=',')
        else:
            total += sumtree(i, trace)
    return total


if __name__ == __name__:
    print(sumtree([1, [2, [3, 4], 5], 6, [7, 8]]))
    print(sumtree([1, [2, [3, 4], 5], 6, [7, 8]], trace=True))
