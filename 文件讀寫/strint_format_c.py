
file_in=open("e:\c_key.txt","r")
file_out=open("e:\c_out","w")

a=file_in.readlines()
str=""

for i in a:
    str+=i

str.split(sep=' ')
print(str)