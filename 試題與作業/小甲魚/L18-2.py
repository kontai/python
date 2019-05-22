# 编写一个函数 findstr()，该函数统计一个长度为 2 的子字符串在另一个字符串中出现的次数。
# 例如：假定输入的字符串为“You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted.”，
# 子字符串为“im”，函数执行后打印“子字母串在目标字符串中共出现 3 次”

def findstr(desStr, subStr):
    count = 0
    if subStr not in desStr:
        print("未找到符合字符串!")
    else:
        for i in range(len(desStr) - 1):
            if desStr[i] == subStr[0] and desStr[i + 1] == subStr[1]:
                count += 1
                i += 1
        print("子字母串出現在目標字串符中%d次" % count)


desStr = input('請輸入目標字符串: ')
subStr = input('請輸入子字符串(兩個字符): ')
findstr(desStr, subStr)
