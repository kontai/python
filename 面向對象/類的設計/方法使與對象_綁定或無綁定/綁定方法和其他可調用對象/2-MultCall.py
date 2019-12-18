#  Copyright (c) 2019.
#  2-MultCall.py
#

def square(arg):
    return arg ** 2  # Simple,functions (def or lambda)


class Sum:
    def __init__(self, val):  # Callable instances
        self.val = val

    def __call__(self, arg):
        return self.val + arg


class Product:
    def __init__(self, val):
        self.val = val

    def method(self, arg):
        return self.val * arg


# 調用來產生實例
class Negate:
    def __init__(self, val):
        self.val = -val

    def __repr__(self):
        return str(self.val)


sobject = Sum(2)
pobject = Product(3)
actions = [square, sobject, pobject.method]
for act in actions:
    print(act(5))
print(actions[-1](5))
print([act(5) for act in actions])
print(list(map(lambda act: act(5), actions)))

print("*" * 20)
actions = [square, sobject, pobject.method, Negate]
for act in actions:
    print(act(5))
print("*" * 20)
print([act(5) for act in actions])

table = {act(5): act for act in actions}
for (key, value) in table.items():
    print("{0} => {1}".format(key, value))
