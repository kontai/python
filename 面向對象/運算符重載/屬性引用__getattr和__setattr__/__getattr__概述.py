#  Copyright (c) 2019.
#  Age.py
#
"""
__getattr__方法是攔截屬性點號運算。
當通過對未定義（不存在）屬性名稱和實例進行點號運算時，就會用屬性名稱作為字符串調用這個方法。
如果Python可通過其繼承樹搜索找到這個屬性，該方法就不會被調用。
"""


class empty:
    def __getattr__(self, attrname):
        if attrname == "age":
            return 40
        else:
            raise AttributeError(attrname)


X = empty()
print(X.age)
print(X.name)
