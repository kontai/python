#  Copyright (c) 2019.
#  pickleLoad.py
#

import pickle

obj = pickle.load(open("shopfile.dat", "rb"))
print(obj.server, obj.chef)
print(obj.order("Sue"))
