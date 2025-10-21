# # exec (Not recommended, not secure)
# module='string'
# exec('import '+module)
# print(string)
#
# #__import__
# moduleName='string'
# string=__import__(moduleName)
# print(string)

#importlib (Recommend)
import importlib
moduleName='string'
string=importlib.import_module(moduleName)
print(string)
