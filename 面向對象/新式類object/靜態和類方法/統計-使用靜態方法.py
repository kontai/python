#  Copyright (c) 2019.
#  統計.py
#

class spam:
    numInstance = 0
    member = []

    def __init__(self):
        spam.numInstance += 1

    def printNumInstance():
        print("Number of Instance:", spam.numInstance)

    printNumInstance = staticmethod(printNumInstance)


# 子類集成定制靜態方法
class sub(spam):
    def printNumInstance():
        print("Extra stuff...")
        spam.printNumInstance()

    printNumInstance = staticmethod(printNumInstance)


# 類可以繼承靜態方法而不用重新定義他把，他可以沒有一個實例而運行，不管定義於類樹的何處
class other(spam): pass


if __name__ == "__main__":
    a = spam()
    b = spam()
    c = spam()
    spam.printNumInstance()
    a.printNumInstance()

    print("-" * 40)

    a = sub()
    b = sub()
    a.printNumInstance()
    sub.printNumInstance()
    spam.printNumInstance()

    print("-" * 40)

    c = other()
    c.printNumInstance()
    other.printNumInstance()
