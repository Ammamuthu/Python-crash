# def num():
#     a=1
#     b=2
#     c=a+b
#     return c
#     return a
# var=num()
# print(var)

def num():
    a=1
    b=2
    c=a+b
    yield c
    yield a
var=num()
print(next(var))
print(next(var))
