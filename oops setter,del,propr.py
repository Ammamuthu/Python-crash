class employee():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=f"{fname}{lname}@gmail.com"
    @property
    def email(self):
        return f"asdfghjkl;"
    def explain(self):
        return f"this is a mail of{self.fname} {self.lname}"
el=employee("coding","bro")
e1.fname="dsssssssssssss"
print(el.email)