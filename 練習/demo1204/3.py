dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1)

dict2={"e":4,"f":5,"a":"winner"}
print(dict2)

dict1.update(dict2)
del dict1["a"]
print(dict1)

dict2tuple=tuple(dict1.keys())
print(dict2tuple)
s01='.'.join(dict2tuple)
print(s01)
