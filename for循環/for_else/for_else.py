import sys

# 當for迴圈正常執行完畢後，會執行else區塊的程式碼
data_list = [11, 22, 33, 44, 55]
for i in data_list:
    print(i)
    break
else:
    print("for迴圈執行完畢")
print(sys.version)

