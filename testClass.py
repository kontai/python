#  coding=utf-8
class TestClass:
    """
    類的實例....
    類封裝
    類靜態方法
    類方法
    """

    def __init__(self, aa=0, bb=0):
        self.aa = 22
        self.bb = 33

    def Area(self):
        print(self.aa * self.bb)

    '''類封裝(裝飾)'''

    @property
    def get_val(self):
        return self.aa

    @get_val.setter
    def get_val(self, a):
        if not isinstance(a, int):
            raise TypeError("not integet")
        elif a > 0:
            self.aa = a

    '''靜態方法'''

    @staticmethod
    def read_val(**exam):
        for na, sc in exam.items():
            print("name=", na, " , score=", sc)

    '''類方法'''

    @classmethod
    def call_in(cls, **aaaa):
        return cls.read_val(**aaaa)

    @classmethod
    def call_get(cls, get_val):
        return cls.get_val

    ''' 類方法無法調用實例方法'''

    def just_print():
        print("test", self.aa)

    @classmethod
    def call_inst(cls):
        cls.just_print()


if __name__ == "__main__":
    print(TestClass.__doc__)
    tc = TestClass()
    # print(tc.get_val)
    # tc.get_val = 20
    # print(tc.get_val)
    data = {"tai": 100, "jay": 30, "yan": 90}
    # tc.read_val(**data)
    tc.call_inst()
    tc.call_in(**data)
    tc.call_get = 33333
    print(tc.call_get)
