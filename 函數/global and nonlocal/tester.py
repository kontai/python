def tester(start):
    state=start
    def nested(label,state):
        print(label,state)
        #local variable 'start' referenced before assignment
        state=+1
    return nested

def testWithNonlocal(start):
    state=start
    def nested(label):
        nonlocal state
        print(label,state)
        state+=1    #每次調用都會產生新的state對象
    return nested

# F=testWithNonlocal(0)
F=testWithNonlocal(0)
F('spam')
F('egg')
F('ham')
