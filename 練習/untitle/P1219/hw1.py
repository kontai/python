#建立一個名為mystery的unicod字串

import unicodedata
name=unicodedata.name('\U0001f4a9')
code=unicodedata.lookup(name)
print(f'name = {name} , code = {code}')