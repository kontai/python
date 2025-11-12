import sys
import math

# tpl = "i am {name}, age {age}, really {name}".format(name="seven", age=18)
#
# tpl = "i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 18})

# 添加鍵 屬性和偏移量
# tpl="My {1[spam]} runs {0.platform}".format(sys,{"spam":"laptop"})
# tpl="My {config[spam]} runs {sys.platform}".format(sys=sys,config={"spam":"laptop"})
#
# somlist=list("SPAM")
# parts=somlist[0],somlist[1],somlist[1:3]
# tpl="first={0},last={1},middle={2}".format(*parts)
#
# "i am {1:>10},age {0:>20}".format("seven",10) #(符號: > 向右對齊  <向左對齊 ^置中)
# "{0:e},{0:.3e},{0:g}".format(math.pi)

# tpl = "i am {:s}, age {:d}".format(*["seven", 18])
# tpl = "i am {:s}, age {:d}".format("seven", 18) #["seven", 18]

print("{0:X}, {1:o}, {2:b}".format(255, 255, 255))
print(bin(255), int('11111111', 2), 0b11111111)
print(hex(255), int('FF', 16), 0xFF)
print(oct(255), int('377', 8))

print("{0:.{1}f}".format(1 / 3.0, 4))
print("%.*f" % (4, 1 / 3.0))
print(format(1 / 3.0, '.4f'))  # 適用單獨項

"{0:,d}".format(99999999999)
