import time

def timmer(func):
    def wrap(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print("運行時間%s"%(stop_time-start_time))
        return res
    return wrap

@timmer
def test(name,age):
    time.sleep(3)
    print("test函式運行完畢！name={%s},age={%s}"%(name,age))
    return "test() return..."

@timmer
def test2(name,age,gender):
    time.sleep(3)
    print("test函式運行完畢！name={%s},age={%s},gender={%s}"%(name,age,gender))
    return "test() return..."
#res=timmer(test)

res=test('kontai',18,)
res=test2('kontai',18,'male')
print(res)
