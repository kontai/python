class CardHolder:
    acctlen = 8          # 類別層級資料（帳號長度）
    retireage = 62.5     # 退休年齡標準

    def __init__(self, acct, name, age, addr):
        self.acct = acct       # 觸發 setter！
        self.name = name       # 觸發 setter！
        self.age = age         # 觸發 setter！
        self.addr = addr       # 普通屬性（不受管理）

    # --- name ---
    def getName(self):
        return self.__name

    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value

    name = property(getName, setName)  # 或用 @property 裝飾器

    # --- age ---
    def getAge(self):
        return self.__age

    def setAge(self, value):
        if value < 0 or value > 150:
            raise ValueError('invalid age')
        else:
            self.__age = value

    age = property(getAge, setAge)

    # --- acct ---
    def getAcct(self):
        return self.__acct[:-3] + '***'   # 隱藏最後三位

    def setAcct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('invalid acct number')
        else:
            self.__acct = value

    acct = property(getAcct, setAcct)

    # --- remain（虛擬屬性）---
    def remainGet(self):
        return self.retireage - self.age  # 即時計算剩餘年數

    remain = property(remainGet)          # 唯讀屬性
