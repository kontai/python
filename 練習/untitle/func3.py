from colorama import Fore
from colorama import Back
from colorama import Style

animal = "cat"

def global_var():
    ''' doc '''
    # global animal
    animal = 'dog'
    print("in function animal:", animal)
    print("locals:", locals())
    print("global:", globals())
    return

global_var()
print(animal)
print("global name:", Fore.RED + Back.CYAN + global_var.__name__)
# 重置
print(Style.RESET_ALL)
print("ABC")
print("global_var __doc__ = "+global_var.__doc__)
print("abc"+"def  ".strip())
# print("global:",globals())
