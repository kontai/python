import numpy as np


arr=np.array([1,2,3,4,5.0])

print(arr)  #印出陣列
print(arr[1:3])


print(arr.shape)    #印出陣列的元素
print(arr.dtype)    #印出陣列的資料型態
print(arr.size) #印出陣列的元素個數
print(arr.ndim) #印出陣列的維度
arr.fill(0)
print(arr)
print(type(arr))