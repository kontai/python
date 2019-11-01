#  Copyright (c) 2019.
#  privateAttr.py
#

# 避免實例內的命名空間的衝突，而不是限制變量名的讀取。

'''
變量名壓縮:
expample: Spam類內__X這樣的變量名會自動變成_Spam__X,原始的變量名會在頭部加入一個下劃線，然後是所在類名稱。
'''


class B1:
    def meth1(self): self.X = 88

    def meth2(self): print(self.X)


class B2:
    def metha(self): self.X = 99

    def methb(self): print(self.X)


class B3(B1, B2): pass


class C1:
    def meth1(self): self.__X = 88

    def meth2(self): print(self.__X)


class C2:
    def metha(self): self.__X = 99

    def methb(self): print(self.__X)


class C3(C1, C2): pass


J = B3()
# self.X所得到的值，取決於最後一個賦值是哪個類。
# 因為所有對self.X的賦值語句都是引用一個相同實例。
# X屬性只有一個(J.X)，無論
J.meth1();
J.metha()
print(J.__dict__)
J.meth2();
J.methb()

I = C3()
I.meth1();
I.metha()  #
print(I.__dict__)
I.meth2();
I.methb()
