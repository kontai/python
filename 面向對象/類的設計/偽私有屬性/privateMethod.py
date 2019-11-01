#  Copyright (c) 2019.
#  privateMethod.py
#

# 如果一個方法傾向於只在一個可能混合到其他類的類中使用，在前面使用雙下劃線
# 以確保該方法不會受到樹中的其他名稱的干擾，特別是在多繼承的環境中。

class Super:
    def mehtod(self): print("In Super class..")


class Tool:
    def __method(self): print("In Tool class..")

    def other(self): self.__method()


class Sub1(Tool, Super):  # 超類依從左到右順序搜索(此處首選Tool)
    def action(self): self.method()


class Sub2(Tool):
    def __init__(self): self.method = 99


if __name__ == '__main__':
    A = Sub1()
    # A.action()

    B = Sub2()
    B.other()
