class School:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.course_list = []

    @staticmethod
    def test(a, b):
        print(a, b)

    @property
    def test2(self):
        print(self.name)


class Course:
    def __init__(self, name, price, period, WTF):
        self.name = name
        self.price = price
        self.period = period
        self.WTF = WTF


if __name__ == '__main__':
    s1 = School('kontai', '桃園')
    s2 = School('tai', '大圜')

    c1 = Course(s1.name, 1000, 2, s1)

    print(c1.__dict__)
    print(c1.WTF.name)

    s1.test(2, 3)
    School("abc", "def").test(3, 4)
    s1.test2
