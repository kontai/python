#  Copyright (c) 2019.
#  foo.py
#
# __all__:它是一个string元素组成的list变量，(通常於__init__.py裡設置)
# 定义了当你使用 from <module> import * 导入某个模块的时候能导出的符号（这里代表变量，函数，类等）。

__all__ = ['bar', 'baz']  # 明確了導出bar,baz

waz = 5
bar = 10


def baz(): return 'baz'
