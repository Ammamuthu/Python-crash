from abc import ABC, ABCMeta,abstractmethod
class codition(metaclass=ABCMeta):
    @abstractmethod
    def shapes(self):
        return 0
        

class square(codition):
    type=4
    type="square"
    def __init__(self):
        self.sid=10

    def shapes(self):
        return f"  {self.sid*self.sid}"
s1=square()
print(s1.shapes())