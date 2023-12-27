#python

def f(T):
    (a, (b, c))=T
    print("{ta}{tb}{tc}".format(ta=a, tb=b, tc=c))
    print("{0}{1}{2}".format(a,b,c))
    s= "%6d %6d %6d"%(a,b,c)


f((1,(2,3)))