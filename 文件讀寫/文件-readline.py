old_file=open("cpy.py","r",encoding='utf-8')

rl=old_file.readline()
print("1: %s"%rl)

rl=old_file.readline()
print("2: %s"%rl)

print('*'*100)

rls=old_file.readlines()
print("readlines: \n%s"%rls)

print(len(rls))
