a=[100]

def test(num):
    #臨時變量+=全局變量  全局變量在運算時已經被改變,離開函數體後,a指向修改後的值
    num+=num  #num指向新的值[100,100]
    #num = num + num   #num + num 的結果 , 賦予臨時變量 num
    print(num)
test(a)
print(a)

######################

b=100

def test2(num):
    #臨時變量+=全局變量  因全局變量為常數,無法修改,運算後的值將交給臨時變量
    num+=num  #
    #num=num+num
    print(num)
test2(b)
print(b)