class Person:
    def __init__(self, name):
        self.hide_name = name


class Mailman(Person):
    def __init__(self, name, mail):
        # super().__init__(name)
        self.__name = name
        self.mail = mail

    @property
    def name(self):
        'i am property'
        print("inside the getter")
        return self.__name

    @name.setter
    def name(self, name):
        print("inside the setter")
        self.__name = name


if __name__ == '__main__':
    new_person = Person("tai")
    new_mailman = Mailman("joe", "test@test.test")
    # print(f'name={new_mailman.name}\nmail={new_mailman.mail}')
    new_mailman.name = "kontai"
    print(new_mailman.name)
    print(new_mailman.__dict__)
