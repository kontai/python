#  Copyright (c) 2019.
#  callee.py
#

"""
如果定義了,Python就會為實例應用函數調用表達式運行__call__方法。
讓類實例的外觀和用法類似於函數
"""


class Callee:
    def __call__(self, *args, **kwargs):
        print("Called: ", args, kwargs)


C = Callee()
print(C(1, 2, 3))
print(C(1, 2, 3, x=4, y=6))
print(C(*[1, 2], **dict(c=3, d=4)))
