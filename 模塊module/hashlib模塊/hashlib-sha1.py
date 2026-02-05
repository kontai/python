import hashlib
import time

_data = "my name is kontai"

def customer_sha1(data):
    if isinstance(data,str):
        _data=data.encode('utf8')
    elif isinstance(data,bytes):
        _data=data
    else:
        raise TypeError('data must be str or bytes')
    _timestamp=str(int(time.time()))
    _sha1_data=hashlib.sha1(_data+_timestamp)
    _res=_sha1_data.hexdigest()
    return _res.decode('utf8')

