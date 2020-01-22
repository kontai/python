#  Copyright (c) 2019.
#  readDoc.py
#

import 文檔字符串.docstr as docstr

print(docstr.__doc__)
print(docstr.func.__doc__)
print(docstr.spam.__doc__)
print(docstr.spam.method.__doc__)

print('\n', '*' * 50, '\n')
help(docstr)

import numpy
