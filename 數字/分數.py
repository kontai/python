from fractions import Fraction

'''
分數的創建
'''
x=Fraction(1,3)
y=Fraction(4,6)

print(x)
print(y)

print('*'*20)
'''
分數的運算
'''
print('x+y= ',x+y)
print('x--= ',x-y)
print('x*y= ',x*y)

print('*'*20)
'''
使用浮點數字創建
'''
print(Fraction('.25'))
print(Fraction('1.25'))
print(Fraction('.25')+Fraction('1.25'))
