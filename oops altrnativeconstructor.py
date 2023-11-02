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
print(win.salary)