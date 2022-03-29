import time
import hashlib
import uuid

def create_md5():
    m = hashlib.md5()
    m.update(bytes(str(time.time()), encoding='utf-8'))
    return m.hexdigest()

def create_sha():
    m = hashlib.sha256()
    m.update(bytes(str(time.time()), encoding='utf-8'))
    return m.hexdigest()

def create_uuid():
    return str(uuid.uuid1())

if __name__ == '__main__':
    # print("%-6s: %s" % ('uuid',create_uuid()))
    # print("%-6s: %s" % ('sha256',str(create_sha())))
    # print("%-6s: %s" % ('md5',create_md5()))
    file=open('01.py','rb')
    content=file.read()
    md5_m=hashlib.md5()
    md5_m.update(content)
    print(md5_m.hexdigest())