import hashlib

data = "asdfasldfkhj".encode("utf8")
md5_obj = hashlib.md5()
md5_obj.update(data)
data2 = "this is test texxt".encode("utf8")
md5_obj.update(data2)
h = md5_obj.hexdigest()
print(h)
