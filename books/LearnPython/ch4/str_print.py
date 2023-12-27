import sys
reply = """
Greeting...
Hello %(name)s!
Your ae squared is %(age)s
"""
values = {'name': 'bob', 'age': 40}

print(reply % values)

print(vars())

print("%(name)s %(age)d" % values)

print("{1[spam]} = {0.platform}".format(sys,{'spam':'fred'}))
