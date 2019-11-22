#  Copyright (c) 2019.
#  trace.py
#

class wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attrname):
        print("Trace: ", attrname)
        return getattr(self.wrapped, attrname)


if __name__ == '__main__':
    x = wrapper([1, 2, 3])
    x.append(4)
    print(x.wrapped)

    x = wrapper({"a": 1, "b": 2})
    print(x.keys())

    u = range(10000)
    import time

    for_timer = 0
    map_timer = 0
    for i in range(10):
        time_start = time.time()
        aa = wrapper(range(10000))
        list(map(lambda x: x * 2, u))
        for_timer += time.time() - time_start

        time_start = time.time()
        bb = wrapper(range(10000))
        list(a * 2 for a in u)
        map_timer += time.time() - time_start
    print(for_timer / 10.0)
    print(map_timer / 10.0)
    print("Faster: ", "for_timer" if for_timer < map_timer else "map_timer")
