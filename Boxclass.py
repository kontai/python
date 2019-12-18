###!/usr/bin/python3
# -*- coding:utf-8 -*-
import random
import os


def foo(self):
    return self._foo


class Box:
    __cnt = 0

    def __init__(self):
        self.lenth = 0
        self.width = 0
        self.height = 0

    def cct(self):
        Box.__cnt += 1
        result = self.lenth * self.width * self.height
        # print("第",Box.__cnt,"次計算結果:",result,"\n")
        return str("第" + str(Box.__cnt) + "次計算結果:" + str(result) + "\n")


# write_to = "/home/kontai/下載/output"
write_to = "e:\\1.txt"
file_w = open(write_to, "w")
if __name__ == "__main__":
    bc = Box()
    i = int(input("請輸入計算次數:"))
    while i > 0:
        bc.lenth = random.randint(0, 100)
        bc.width = random.randint(0, 100)
        bc.height = random.randint(0, 100)
        if bc.lenth * bc.width * bc.height == 0:  # 不可為0
            continue
        print("lenth=", bc.lenth, ",width=", bc.width, ",height=", bc.height,
              "\n")
        st = bc.cct()
        print(st)
        file_w.write(st)
        i -= 1
file_w.close()
