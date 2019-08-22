#類for循環嵌套
A=list(x+y for x in [0,1,2] for y in [100,200,300])
print(A)

M=[[1,2,3],
   [4,5,6],
   [7,8,9]]

N=[[2,2,2],
   [3,3,3],
   [4,4,4]]


print(M[1])
print(M[1][2])

A=list(row[1] for row in M)
print(A)

B=list(M[x][x] for x in range(len(M)))
print(B)

C=list(M[x][y]*N[x][y] for x in range(len(M)) for y in range(len(N)))
print(C)

D=list([M[x][y]*N[x][y] for x in range(len(M))] for y in range(len(N)))
print(D)

