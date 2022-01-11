import os

# fout = open('oops.txt', 'wt')
# print('oops! i created a file', file=fout)
# fout.close()
from shutil import copy

# print(os.path.exists('oops.txt'))
# for p in os.path.__dict__:
#     print(p)

# copy('oops.txt','oops2.txt')
# os.link('oops.txt','oops')

print(os.path.isfile('oops'))
print(os.path.islink('oops'))

# os.symlink('oops.txt','sym')
# print(os.path.islink('sym'))

print(os.path.abspath('oops.txt'))
print(os.path.abspath('..'))
dir = os.listdir('.')
for file in dir:
    print(file)

# os.mkdir('demo'
# os.chdir('demo')
# fout = open('the_good_man', 'wt')
# fout.write('''Cheerful and happy was his mood,
#            He to the poor was kind and good,
#            And he oft' time did find them food,
#            Also supplies of coal and wood,
#            He never spake a word wad rude,
#            And cheer's those did o;er sorrows brood
#            ''')
# fout.close()
dir = os.listdir('.')
for f in dir:
    print(f,os.path.isfile(f))
