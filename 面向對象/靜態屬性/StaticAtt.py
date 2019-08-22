class Room:
    def __init__(self,name,owner,length,width,heigh):
        self.name=name
        self.owner=owner
        self.length=length
        self.width=width
        self.heigh=heigh

    @staticmethod
    def fun1(name):
        return name

    @property
    def calc_Area(self):
        return self.length*self.width*self.heigh

    @classmethod
    def calc(cls,x):
        print(x.name)

r1=Room('toilet','kontai',20,30,40)
r2=Room('bedroom','kontai',40,60,80)

print(r1.calc_Area)
print(r1.fun1('aaa'))
Room.calc(r1)
# Room.calc(100,3,44)
# r1.calc(2,3,4)
# print(r1.calc_Area)
# print(r2.calc_Area)
