#  Copyright (c) 2019.
#  __setattr__概述.py
#
"""
重載方法__setattr__會攔截所有屬性的賦值語句。
如果定義這個方法，self.attr=value 會變成 __setattr__('attr',value)。
要注意:
    在__setattr__中對任何self屬性作賦值，都會再調用__setattr__，導致了無窮遞歸循環(直至堆棧溢出異常)。

    **如果要使用這個方法，要確保是通過對屬性字典作索引運算來賦值任何實例屬性
      也就是說，是使用self.__dict__['name']=x , 而不是self.name=x
"""


class accesscontrol:
    def __setattr__(self, attr, value):
        if attr == "age":
            self.__dict__[attr] = value
        else:
            raise AttributeError(attr + ' not allowed')


X = accesscontrol()
X.age = 40
print(X.age)
X.name = "mel"
