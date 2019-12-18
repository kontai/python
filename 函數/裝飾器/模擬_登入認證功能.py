import time

# auth_info = [{'name': 'kontai', 'password': 123}, {'name': 'bill', 'password': 123},
#             {'name': 'admin', 'password': 'admin'}]

status = 0
start_time = time.time()


def auth_log(func):
    file = open('abc.txt', 'r')
    auth_info = eval(file.read())
    print(auth_info)

    def wrap(*args, **kwargs):
        global status

        if (status == 0 or time.time() - start_time > 20):
            acc = input('請輸入帳號=>').strip()
            passw = input('請輸入密碼=>').strip()
            for i in auth_info:
                if (i['name'] == acc and str(i['password']) == passw):
                    status = 1
                    print("目前已執行時間:%f" % (time.time() - start_time))
                    return func(*args, **kwargs)
            else:
                print("帳號或密碼錯誤")

        print(acc, passw)
        return func(*args, **kwargs)

    return wrap


@auth_log
def index(name):
    print("親愛的%s,歡迎來到XX購物網" % name)
    time.sleep(3)
    return "do re mi fa so"


@auth_log
def home(name):
    print("Hello~%s,您目前位於[首頁]" % name)
    time.sleep(1)
    return home


@auth_log
def shopping_car(name):
    print("hey,%s,購物車裡有 [飲料][零食][生活用品] 共%d項" % (name, 5))
    time.sleep(1)
    return shopping_car


@auth_log
def order():
    pass


name = 'kontai'
# print(index(name))
index(name)
home(name)
shopping_car(name)
