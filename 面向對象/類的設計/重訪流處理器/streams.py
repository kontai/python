#  Copyright (c) 2019.
#  streams.py
#

"""
以這種方式編寫代碼，讀取器和寫入器對象會內嵌在類實例當中(組合)
我們是在子類內提供轉換器的邏輯，而不是傳入一個轉換器函數(繼承)。
"""


class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while 1:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):  # 抽象方法
        assert False, "converter must be defined"  # Or raise exception
