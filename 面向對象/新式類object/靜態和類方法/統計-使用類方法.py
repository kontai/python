#  Copyright (c) 2019.
#  統計-使用類方法.py
#

class spam:
    numInstance = 0

    def __init__(self):
        spam.numInstance += 1

    def printNumInstance(cls):
        print("Number of instance:", cls.numInstance)

    printNumInstance = classmethod(printNumInstance)


if __name__ == "__main__":
    a, b = spam(), spam()
    a.printNumInstance()  #Passes class to first argument
    spam.printNumInstance()  #Also passes class to first argument
