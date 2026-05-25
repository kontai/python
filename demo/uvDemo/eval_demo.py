from datetime import datetime
d=datetime.now()
dt =str(d)
edt=eval('datetime.now()')

print(type(dt),dt)
print(type(edt),edt)
