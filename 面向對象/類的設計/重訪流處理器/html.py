#  Copyright (c) 2019.
#  html.py
#

# 可以傳入包裝在類中的任何對象（該對象定義了所需要的輸入和輸出方法接口）。

from 面向對象.類的設計.重訪流處理器.converters import Uppercase


class HTMLize:
    def write(selfs, line):
        print("<PRE>%s</PRE>" % line.rstrip())


if __name__ == '__main__':
    Uppercase(open("spam.txt"), HTMLize()).process()
