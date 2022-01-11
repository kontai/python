import struct
img=open("O'Reilly_logo.png",'rb')
rl=img.read()[0:30]
# print(rl[0:30])
width,height=struct.unpack('>LL',rl[16:24])
print(f'valid PNG ,width {width}, height {height}')