class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary += self.salary * percent

    def work(self):
        print(self.name, 'does stuff')

    def __repr__(self):
        return (f'<{self.__class__.__name__}: '
                f'name="{self.name}", salary={self.salary:,.2f}>')


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)
        # super().__init__(name, 50000)

    def work(self):
        print(self.name, 'makes food')


class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)
        # super().__init__(name, 40000)

    def work(self):
        print(self.name, 'interfaces with customer')


class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)
        # super().__init__(name)

    def work(self):
        print(self.name, 'makes pizza')


if __name__ == '__main__':
    pat = PizzaRobot('pat')
    print(pat)
    pat.work()
    pat.giveRaise(0.20)
    print(pat)
    print('{:-^30}'.format('分割符'))
    for klass in Employee, Chef, Server, PizzaRobot:
        object = klass(klass.__name__)
        object.work()

