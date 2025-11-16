class Person:
    def __init__(self, name):              # 在建立物件時觸發
        self._name = name                  # 注意：也會觸發 __setattr__！

    def __getattr__(self, attr):           # 當屬性不存在時觸發
        print('get: ' + attr)
        if attr == 'name':                 # 攔截 name
            return self._name              # 取真實屬性，不會遞迴
        else:                              # 其他屬性 → 錯誤
            raise AttributeError(attr)

    def __setattr__(self, attr, value):    # 在任何屬性指派時觸發
        print('set: ' + attr)
        if attr == 'name':
            attr = '_name'                 # 改成內部屬性名稱
        self.__dict__[attr] = value        # 用 __dict__ 避免遞迴

    def __delattr__(self, attr):           # 在屬性刪除時觸發
        print('del: ' + attr)
        if attr == 'name':
            attr = '_name'                 # 同樣避免遞迴
        del self.__dict__[attr]            # 真正刪除（較少用）


if __name__ == '__main__':
    sue = Person('Sue Jones')  # 建立 sue，具受控屬性
    print(sue.name)  # 觸發 __getattr__
    sue.name = 'Susan Jones'  # 觸發 __setattr__
    print(sue.name)
    del sue.name  # 觸發 __delattr__

    print('-' * 20)

    bob = Person('Bob Smith')  # bob 的屬性運作方式相同
    print(bob.name)

    # print(Person.name.__doc__)       # 無法像 property 那樣存取文件字串
