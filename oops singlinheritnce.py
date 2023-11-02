# class employee():
#     working=12
#     def __init__(self,aname,avalue,adegree):
#         self.name=aname
#         self.age=avalue
#         self.degree=adegree

#     def printdetails(self):
#         return f" a value of name is {self.name} a age of candidate is {self.value}"
    
# ashok=("ashok", 21,"mbbs")
# vijay=("vijay",45, "mcom")

# class newbie(employee):
#     def __init__(self,aname,avalue,adegree,acourse):
#         self.name=aname
#         self.age=avalue
#         self.degree=adegree
#         self.cousre=acourse 
    
#         pass
# common=newbie("sssss",22,"aaaaaaaaaa",3)
# print(common.printdetails())
    
    
class employee():
    working=12
    def __init__(self,aname,asalary,adegree):
        self.name=aname
        self.salary=asalary
        self.degree=adegree
        
    def printdetails(self):
        return f" a value of {self.name}, aamount of {self.salary}, a qualification of {self.degree}"
        
    @classmethod
    def spliter(cls,a):
        spliting=a.split("-")
        return cls(spliting[0],spliting[1],spliting[2])

sky=employee("ashok",4000000,"b.e")
win=employee.spliter("rar-5555550-mms")
class newbie(employee):
    def __init__(self,aname,asalary,adegree,acourse):
        self.name=aname
        self.salary=asalary
        self.degree=adegree
        self.cousre=acourse 
    

    def printdet(self):
        return f" a value of {self.name}, aamount of {self.salary}, a qualification of {self.degree} {self.cousre}"
        
common=newbie("sssss",22,"aaaaaaaaaa",3)
print(common.printdetails())
print(common.printdet())