#  Copyright (c) 2019.
#  Requests庫入門.py
#

import requests
r=requests.get("http://www.yahoo.com.tw")
print(r.status_code)
print(r.encoding)
print(r.apparent_encoding)
# print(r.text)
print(r.content)