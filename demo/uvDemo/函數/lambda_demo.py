#lamnda 用法一
student_list = [
    {"name": "zhang3", "age": 36},
    {"name": "li4", "age": 14},
    {"name": "wang5", "age": 27},
]

new_student_list = sorted(student_list, key=lambda s: s["age"])
print(new_student_list)


#lambda 用法二
list1=[i for i in range(5)]
newList1=map(lambda x:'tai'+str(x),list1)
print(list(newList1))

#lambda 用法三
list2=[i for i in range(10)]
evenList=filter(lambda x:x%2==0,list2)
print(list(evenList))

#另一種寫法
evenList2=[x for x in list2 if x%2==0]
print(evenList2)
