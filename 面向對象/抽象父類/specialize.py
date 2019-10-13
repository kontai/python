#  Copyright (c) 2019.
#  specialize.py
#

class Super:
    def method(self):
        print("in Super.method")

    def delegate(self):
        self.action()  # 抽象方法

    def action(selfs):
        """
        當子類對象調用action方法,但子類未定義action方法時，觸發父類異常方法
        :return:
        """
        # assert False,'action must be defined!'
        raise NotImplementedError("action must be defined!")


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print("in Replacer.method")


class Extender(Super):
    def method(self):
        print("starting Extender.method")
        Super.method(self)
        print("ending Extender.method")


class Provider(Super):
    def action(self):
        print("in Proveider.action")


class Provider2(Super): pass


if __name__ == "__main__":
    for klass in (Inheritor, Replacer, Extender):
        print("\n" + klass.__name__ + "...")
        klass().method()
    print("\nProvider...")
    x = Provider()
    x.delegate()

    y = Provider2()
    y.delegate()
