#

#由於import只在程式執行時,將模塊一次性的載入記憶體,接下來的import,不會再重新讀取模塊(直接調用記憶體裡的變量或函數)
#利用imp裡的reload函數,可以動態重新讀取該模塊(覆蓋記憶體內的值)
# import import概述.reload_function.mod1
# from import概述.reload_function.mod1 import X
from  import概述.reload_function import mod1
import sys
print(mod1.X)
print(mod1.__dict__['X'])
# print(sys.modules['mod1'].X)
print(getattr(mod1,'X'))
print(mod1)
import imp
imp.reload(mod1)


