# while((x=next()) ! = NULL) {...process x...}


# I
'''
while True:
    x=next()
    if not x:bresk
    ...process x...
'''


# II
'''
x = True
while x:
    x = next()
    if x:
        ...process x...
'''


# III
'''
x = next()
while x:
    ...process x...
    x = next()
'''

