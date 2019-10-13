#  Copyright (c) 2019.
#  updatedb.py
#  File updatedb.py:update Person object on database


import shelve

db = shelve.open("persondb")
for key in sorted(db):
    print(key, '\t=>', db[key])
print(type(db['Sue Jones']))
sue = db['Sue Jones']
sue.giveRaise(.10)
db['Sue Jones'] = sue
db.close()
