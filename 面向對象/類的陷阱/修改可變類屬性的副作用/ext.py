#由於類屬性由所有實例共享，所以如果一個類屬性引用一個可變對象，那麼從任何實例來原處修改該對象都會立刻影響到所有實例。

class C:
    shared=[]
    def __init__(self):
        self.perobj=[]
x=C()
y=C()
print(y.shared,y.perobj)

x.shared.append("spam")
x.perobj.append('spam')
print(x.shared,x.perobj)
print(y.shared,y.perobj)
print(C.shared)


