#  Copyright (c) 2019.
#  converters.py
#

from 面向對象.類的設計.重訪流處理器.streams import Processor


class Uppercase(Processor):
    def converter(self, data):
        return data.upper()


if __name__ == '__main__':
    import sys

    obj = Uppercase(open("spam.txt"), sys.stdout)
    obj.process()
