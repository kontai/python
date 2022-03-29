import os
p=os.path.abspath(__file__)
print(p)
print(os.path.dirname(p))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
print(os.path.join(BASE_DIR,'Template'))