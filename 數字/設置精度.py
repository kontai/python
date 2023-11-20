import decimal

print(decimal.Decimal(1)/decimal.Decimal(7))    #設置精度前

decimal.getcontext().prec=4 #設置精度

print(decimal.Decimal(1)/decimal.Decimal(7))    #設置精度前
