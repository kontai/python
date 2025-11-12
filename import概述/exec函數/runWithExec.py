modename = "string"
###################
# exec("import "+modename)
###################


# 使用__import__速度更快
string = __import__(modename)
string
print(string)
