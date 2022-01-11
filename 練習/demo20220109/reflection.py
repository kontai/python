class FTPdemo:
    def __init__(self,*ip):
        self.a=ip[0]
        self.b=ip[1]
        self.c=ip[2]

a=FTPdemo(1,2,3)
print(a.d)
# if hasattr(a,'d'):
# else:
#     print("no d")
