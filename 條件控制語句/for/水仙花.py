i=0;j=1
print(i,end=' ')
for cnt in range(100):
    if cnt%8==0:
        print()
    print("%22d"%j,end=' ')
    j=j+i
    i=j-i
