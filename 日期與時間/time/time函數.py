import time

#顯示由1970年1月1日至今的秒數 (又稱為epach)
now=time.time()
print(now)

#將epach轉換為字串
nowCT=time.ctime()
print(nowCT)

#系統時區時間
print(time.localtime())

#UTC時間
print(time.gmtime())

#格式互轉(因精準度只到秒<與上面的epach有差異>)
print(time.mktime(time.gmtime()))