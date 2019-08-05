city = {
    "桃園": {},
    "台北": {}
}
path = []
while True:
    temp = city
    for i in path:
        temp = temp[i]
    print("目前所在地=>", list(temp.keys()))
    option = input("1.查詢位置 2.增加位置 <返回(B)/退出(Q)")
    if option == "1":
        v = input("請輸入想查詢位置=>")
        path.append(v)

    elif option == "2":
        pass
    elif option == 'b':
        pass
    elif option == 'q':
        break;
    else:
        print("輸入錯誤！！")
