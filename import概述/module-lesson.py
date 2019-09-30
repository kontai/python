

# from web.web1.web3 import cal
#from web.web1.web3.cal import add

# from web.web1 import web3   #执行web3的__init__文件,唯一不支持的调用方式
# print(web3.cal.add(2,6))



from web.web1.web3 import cal


print(cal.add(3,8))
print(cal.__name__,cal.__file__,sep='\n')







