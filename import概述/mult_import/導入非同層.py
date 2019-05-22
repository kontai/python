import os,sys

#不允許絕對路徑（寫死了）
#sys.path.append(r"D:\workspace\python\import概述\day21_lesson")

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from day21_lesson.my_module.cal import add

print(add(2,3))