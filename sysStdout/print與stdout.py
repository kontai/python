import sys

sys.stdout.write("start here using stdout: " + 'a' + 'b' + 'c\n')
print("start here using print: " + 'a' + 'b' + 'c\n')

# 保留原始stdout,以供恢復。
temp = sys.stdout

# 將輸出流綁定於文件輸出流，接下來的print都會輸出至文件。
sys.stdout = open("test.txt", "w")

print('a', 'b', 'c', sep=',')
print('d', 'e', 'f', sep=',')

print('format: %s %-3d %05.9f' % ("test file", 3.14, 3.14))
print(temp)

# recover stdout stream
sys.stdout = temp

print('a', 'b', 'c')
print("test file output", file=open('test.txt', 'a'))
open('test.txt', 'a').write('12345')
print(open('test.txt').read())
