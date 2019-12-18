#  Copyright (c) 2019.
#  listerWithDir.py lister.py continued
#

class ListInherited:
    """
    Use dir() to collect both instance attrs and names
    inherited from its classes;Python 3.0 shows more
    names than 2.6 because of the implied object superclasss
    in the new-style class model; getattr() fetches inherited
    names not in self.__dict__;use __str__,not __repr__,
    or else this loops when printing bound methods!
    """

    def __str__(self):
        return "<Instance of %s,address %s:\n%s" % (
            self.__class__.__name__,  # My classs's name
            id(self),  # My address
            self.__attrnames())  # name=value list

    def __attrnames(self):
        result = ""
        for attr in dir(self):  # instance dir()
            if attr[:2] == "__" and attr[-2:] == "__":  # skip internals
                result += "\tname %s=<>\n" % attr
            else:
                result += "\tname %s=%s\n" % (attr, getattr(self, attr))
        return result
