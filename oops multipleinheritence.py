class employee():
    working=12
    def __init__(self,aname,asalry,adegree):
        self.nam=aname
        self.age=asalry
        self.degree=adegree
    def printdetails(self):
        return f"a value of {self.nam} and age of {self.age} {self.degree}"


ashok=employee("ashok",21,"CSE")
arivu=employee("arivu",21,"EEE")
class program:
    pass
    def __init__(self,aname,asalary,adegree,aex):
        self.name=aname
        self.age=asalary
        self.degree=adegree
        self.ex=aex

kraa=program("kraan",21,"fds",11111111111)
class coolguy(employee,program):
    pass
free=coolguy("alex",22,"tamil")

print(ashok.printdetails)