# -*- coding:utf-8 -*-
num1 = [12, 5, 46, 4.5474567, 3, 45, 2312, 2]

order_num=num1
order_num.sort()

print("由小到大排序",order_num)

rev_num=num1
rev_num.sort()

print("由大至小排序",rev_num)

num2=[{'name':'kontai','age':40},{'name':'tai','age':49},{'name':'ggyy','age':30}]
dict_sort=num2
dict_sort.sort(key=lambda a:a['name'])
print("字典排序",dict_sort)