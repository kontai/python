list1 = ['1.Just do it', '2.一切皆有可能', '3.讓邊程改變世界', '4.Impossible is Nothing']
list2 = ['4.Adidas', '2.李寧', '3.Fish C', '1.Nike']

'''
將兩組list一以下格式儲存於list3
['1.Nike:Just do it']
['2.李寧:一切皆有可能']
['3.Fish C:讓邊程改變世界']
['4.Adidas:Impossible is Nothing']
'''

list3 = [[name + ':' + slogan[2:]] for slogan in list1 for name in list2 if name[0] == slogan[0]]

for each in list3:
    print(each)
