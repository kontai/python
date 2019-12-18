#  Copyright (c) 2019.
#  pickleDump.py
#

from 面向對象.類的設計.繼承與組合.pizzashop import PizzaShop

shop = PizzaShop()
print(shop.server, shop.chef)

import pickle

pickle.dump(shop, open("shopfile.dat", "wb"))
