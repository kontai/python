class Adder:
    def __init__(self, x):
        self.data = x

    def __add__(self, x, y):
        print("Not Implemented")


class ListAdder(Adder):
    # def __add__(self, x, y):
    #     return x + y
    def __init__(self, x):
        Adder.__init__(self, x)

    def __add__(self, other):
        return self.data + other


class DictAdder(Adder):
    def __init__(self, x):
        Adder.__init__(self, x)

    def __add__(self, y):
        # self.dic = x
        # for i in y:
        #     self.dic[i] = y[i] if i not in self.dic else str(self.dic[i]) + ',' + y[i]
        # return self.dic

        for i in y:
            self.data[i] = y[i] if i not in self.data else str(self.data[i]) + ',' + y[i]
        return self.data


if __name__ == '__main__':
    # I = Adder()
    # I.__add__(2, 3)

    # u=[1,2,3]
    # y = [3, 4, 6]
    # a = {"a": 12, "b": 22, "c": "ke"}
    # b = {"k": 2, "a": "ko"}
    # A = ListAdder()
    # B = DictAdder()
    # print(A.__add__(u, y))
    # print(B.__add__(a, b))

    u = [1, 2, 3]
    y = [3, 4, 6]
    a = {"a": 12, "b": 22, "c": "ke"}
    b = {"k": 2, "a": "ko"}

    A=ListAdder(u)
    D=DictAdder(a)
    print(A+y)
    print(D+b)

