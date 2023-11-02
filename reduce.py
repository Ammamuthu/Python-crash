

from functools import reduce

def added(x,y):
    return x+y

li=[3,1,2,3,4,5,7,8,9,]
license=reduce(added,li)
print(license)

