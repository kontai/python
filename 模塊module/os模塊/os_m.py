import os
import time

print(os.getcwd())
os.chdir('..')
print(os.getcwd())

# DIR='dir'
# #os.removedirs(DIR)
# os.makedirs(DIR)
# for i in range(1,100):
#     for j in range(1,100):
#         os.makedirs(DIR+'\\'+ DIR+str(i)+'\\'+DIR+str(j))
#         print(DIR+'\\'+ DIR+str(i)+'\\'+DIR+str(j)+'    ok!')
#         #time.sleep(2)
