y = int(input('請輸入數字=> '))
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1

# 當while沒有遇到break時，else才會執行。(循環主體從沒執行過，else也會執行。
else:
    print(y, 'is prime')
