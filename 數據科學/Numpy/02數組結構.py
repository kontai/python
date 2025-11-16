import numpy as np
array=np.array([[1,2,3],
       [4,5,6],
       [7,8,9]])

print(array)
print(array.dtype)
print(type(array))
print(array.shape)
print(array.ndim)
print(array.size)
print('-'*20)

#複製
array2=array.copy()
print(array)
print('-'*20)
print(array2)
print('-'*20)

#切片
print(array[:,1])
print(array[0,0:2])

print('-'*20)
a_array=np.arange(0,100,10)
print(a_array)

#bool
mask=np.array([[0,0,0,1,1,1],],dtype=bool)
print(mask)
mask=a_array>50
print(mask)
print(a_array[mask])    #篩選大於50的元素
print(np.where(a_array>50))
print(a_array[np.where(a_array>50)])
