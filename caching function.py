import time
from functools import lru_cache

@lru_cache
def some(n):
    print("computaying..........")
    time.sleep(1)
    return n*n
var=some(10)
print(var)
var1=some(100)
print(var1)
var2=some(105)
print(var2)
var3=some(10)
print(var3)
