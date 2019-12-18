# -*-coding:utf-8 -*-

print("*" * 15, '\t', "名片登錄系統 V0.001", '\t', '*' * 15)
print("1.新增資料.")
print("2.刪除資料.")
print("3.修改資料.")
print("4.查詢資料.")
print("5.調出所有資料.")

card = list()

# 判斷===>連續輸入兩次,就離開程序
er = 0

while er != 2:
    number = input("請輸入選項:")

    if number == "1":
        new_name = input("Name:")
        new_age = input("Age:")
        new_addr = input("Address:")
        new_tel = input("TEL:")
        new_info = {}
        new_info['name'] = new_name
        new_info['age'] = new_age
        new_info['addr'] = new_addr
        new_info['tel'] = new_tel
        card.append(new_info)
        print(card)

    elif number == "2":
        del_data = input("請輸入要刪除的名字:")
        ind = 0
        for delete in card:
            if del_data == delete['name']:
                del card[ind]
                print("已刪除%s.." % del_data)
                print(card)
            else:
                print("無此資料...")

    elif number == "3":
        pass
    elif number == "4":
        pass
    elif number == "5":
        pass
    else:
        print("無效輸入....")
        er += 1
