#global 引用一個未創建的對象時,會自動創建一個本地對象

def test_global(start):
    def nested(label):
        global state_g
        state_g=0
        print(label,state_g)
    return nested

# def test_nonlocal(start):
#     def nested(label):
#         nonlocal state_n
#         state_n=0
#         print(label,state_n)
#     return nested

F=test_global(0)
F("abc")
print(state_g)



#nonlocal 不會在整個糢塊尋找對象,只會在嵌套函數中查找


# spam=66
# def test_nonFind(start):
#     def nested(label):
#         nonlocal spam
#         print(spam)
#     return nested



