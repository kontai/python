def getNumbers(num):
    if (num > 1):
        return getNumbers(num - 1) * num
    else:
        return num


print(getNumbers(5))
