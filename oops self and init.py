# class employee():
#     pass
#     def somethings(self):
#         return f"a value of name is{self.name} a value of age is {self.age}"

# ammamuthu=employee()
# ashok=employee()

# ammamuthu.name="werid"
# ammamuthu.age=21

# ashok.name="nick"
# ashok.age=21
# print(ashok.somethings())



# """ constructors""""

class employee():
    def __init__(self,name,salary):
        self.person1=name
        self.amount=salary
        pass

kiss=employee("arun",2346789)
vass=employee("jarge",987654321)
print(vass.amount)