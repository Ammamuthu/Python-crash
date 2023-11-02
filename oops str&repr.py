# a="sssssssssssss"
# print(a)
# print(int.__str__(a))
# print(int.__repr__(a))


class employe():
    pass
    def __init__(self,aname,avlue):
        self.name=aname
        self.age=avlue
    def printer(a): 
        return f"avalue of {a.name} and thn a{a.age}"
    def __str__(b):
        return f"avalue of {b.name} and thn a{b.age}"
    def __repr__(d):
        return f"ssdfghjkfghjkfghjkl"

pal=employe("kishan",2)
amigo=employe("ytb",3)
print(repr(pal))