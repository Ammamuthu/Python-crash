# class a:
#     classvar1=" iam a touch guy"
#     def __init__(self):
#         self.var1="mak me really rough guy"

    
# class b(a):
#     classvar2="it's a surly puf  guy"
# A=a()
# B=b()
# print(B.classvar1)


# class a:
#     classvar1=" iam a touch guy"
#     def __init__(self):
#         self.var1="mak me really rough guy"

    
# class b(a):
#     classvar1="it's a surly puf  guy"
#     def __init__(self):
#         pass
#         #self.var1=" iam a bad guy"
        
# A=a()
# B=b()
# print(B.var1)

class a:
    classvar1=" iam a touch guy"
    def __init__(self):
        self.var1="mak me really rough guy"

    
class b(a):
    classvar1="it's a surly puf  guy"
    def __init__(self):
        
        super().__init__()

        self.var1=" iam a bad guy"
    
        
        
        
A=a()
B=b()
print(B.var1)