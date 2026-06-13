from functools import reduce
#map function
numList = [1, 2, 3, 4, 5]
res = map(lambda x: "tai" + str(x), numList)
print(list(res))

#list generator
res2=["tai"+str(x) for x in numList]
print(res2)



