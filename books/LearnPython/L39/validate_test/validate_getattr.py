class CardHolder:
    acctlen = 8          # 類別層級資料
    retireage = 62.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct       # 觸發 __setattr__
        self.name = name
        self.age = age
        self.addr = addr       # 非受管理屬性

    # 攔截未定義屬性（取值）
    def __getattr__(self, name):
        match name:
            case 'acct':
                return self._acct[:-3] + '***'
            case 'remain':
                return self.retireage - self.age
            case _:
                raise AttributeError(name)

    # 攔截所有屬性（賦值）
    def __setattr__(self, name, value):
        match name:
            case 'name':
                value = value.lower().replace(' ', '_')
            case 'age':
                if value < 0 or value > 150:
                    raise ValueError('invalid age')
            case 'acct':
                name = '_acct'
                value = value.replace('-', '')
                if len(value) != self.acctlen:
                    raise TypeError('invalid acct number')
            case 'remain':
                raise TypeError('cannot set remain')
        self.__dict__[name] = value  # 避免遞迴
