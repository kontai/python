#  Copyright (c) 2019.
#  lister.py
#

class ListerInstance:
    """
    Mix-in class that provides a formatted print() or str() of
    instances via inheritance of __str__, coded here;displays
    instance attrs only; self is the instance of lowest class;
    use __X names to avoid clashing with client's attrs
    """

    def __str__(self):
        return '<Instance of %s, address %s:\n%s' % (
            self.__class__.__name__,  # My class's name
            id(self),  # My address(顯示實例的內存地址）
            self.__attrnames())  # name = value list (偽私有)

    def __attrnames(self):
        result = ""
        for attr in sorted(self.__dict__):
            result += '\tname %s=%s\n' % (attr, self.__dict__[attr])
        return result
