print(ord('a'))
print(chr(97))
print(hex(97))  # 16進位顯示，適合8位元
print(0b0111_1111)  #ASCII的7位元上限

'''
Latin-1 (ISO-8859-1)
'''
print(chr(196))

print(ord('➡'))
print(chr(10145))
str=chr(10145)
print(str*20)
emoj=[hex(ord(c)) for c in '🙂🙊👍']
print(emoj)
print(chr(0x1f642))