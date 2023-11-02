# class a:
#     pass
# class b(a):
#     pass
# class c(a):
#     pass
# class d(b,c):
#     pass

class a:
    def fun(self):
        print(" tahis ashjkls")
class b(a):
    pass
class c(a):
    pass
class d(b,c):
    pass
A=a()
B=b()
C=c()
D=d()

print(D.fun())