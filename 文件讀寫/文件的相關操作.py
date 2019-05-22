import os

#文件重命名
os.rename("abc.txt","def.txt")

#刪除文件
os.remove("abc.txt")

#創見資料夾
os.mkdir("test")

#刪除資料夾
os.rmdir("test")

#獲取當前目錄
os.getcwd()

#改變默認目錄
os.chdir("../")  #接下來的文件操作目錄都在"../"

#獲取目錄列表
os.listdir("./")