#  Copyright (c) 2019.
#  InPython3.py
#

# 在python3中,無綁定方法是函數
# 在pytho3.0中，不使用一個實例而調用一個方法沒有問題，只要這個方法不期待一個實例，並且你通過類調用他，而不是通過實例。
# 只有通過實例調用，python3.0才會向方法傳遞一個實例
# 當通過一個類調用的時候，只有在方法期待一個實例的時候，才必須手動傳遞一個實例

class Selfless:
    def __init__(self, data):
        self.data = data

    def selfless(arg1, arg2):  # A simple function in 3.0
        return arg1 + arg2

    def normal(self, arg1, arg2):  # instance expected when called
        return self.data + arg1 + arg2


X = Selfless(2)
print(X.normal(3, 4))  # Instance passed to self automatically
# print(X.selfless(3,4))

# print(Selfless.normal(3,4))
print(Selfless.normal(X, 3, 4))  # self expected by method pass automatically
print(Selfless.selfless(3, 4))  # No instance works in 3.0 , fail in 2.6!
