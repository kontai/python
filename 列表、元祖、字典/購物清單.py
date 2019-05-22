# 简单购物车,要求如下：
# 实现打印商品详细信息，用户输入商品名和购买个数，则将商品名，价格，购买个数加入购物列表，如果输入为空或其他非法输入则要求用户重新输入　

msg_dic = {
    'apple': 10,
    'tesla': 100000,
    'mac': 3000,
    'lenovo': 30000,
    'chicken': 10,
}

temp = []
total_price = 0
while True:
    print("商品列表:")
    for item, i in enumerate(msg_dic.items()):
        print(item, i[0], ' $', i[1])
        temp.append(i[1])
    print("購買總金額: %s"%total_price)
    shop_list = input('請輸入購買項目(\'q\' to exit)=>').strip()
    if(shop_list=='q' or shop_list == 'Q'):
        break
    if (int(shop_list) > len(temp)-1 or int(shop_list)<0):
        print("error")
        continue
    shop_list = int(shop_list)

    shop_num = input('請輸入購買數量(\'q\' to exit)=>').strip()
    if(shop_list=='q' or shop_list == 'Q'):
        break
    if (shop_num.isdecimal()):
        shop_num=int(shop_num)
        total_price += int(temp[shop_list] * shop_num)
    else:
        print("wrong number...")
        continue

