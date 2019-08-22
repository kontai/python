import hashlib

obj=hashlib.md5()

# obj.update("admin".encode("utf8"))
# print(obj.hexdigest())    #21232f297a57a5a743894a0e4a801fc3

obj.update("adminroot".encode("utf8"))
print(obj.hexdigest())#   4b3626865dc6d5cfe1c60b855e68634a
                      #   4b3626865dc6d5cfe1c60b855e68634a

