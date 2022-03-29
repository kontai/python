import os
import sys

BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
print(os.path.join(os.path.dirname(__file__),'01'),'/')