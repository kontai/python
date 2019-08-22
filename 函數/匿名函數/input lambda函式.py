#!/usr/bin/python3
def alg(a,b,aa):
    result=aa(a,b)
    return result

#res=alg(3,5,lambda x,y:x*y)

func_lam=input("lambda func=>")
#eval 函數可以執行某一段字串（String）的運算，如果該字串是運算式，則eval 會計算出運算結果
func_lam=eval(func_lam) #將字串轉成指令
res=alg(3,5,func_lam)

print(res)
