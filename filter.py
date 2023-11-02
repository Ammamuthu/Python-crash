# def greater(d):
#     return d>2
# print(greater(00))

def greater(z):
    return z>5
nm=[1,3,5,6,7,8,9,0,22]
nm=list(filter(greater,nm))
print(nm)