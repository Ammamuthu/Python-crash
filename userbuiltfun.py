'''def add():
    a=1
    b=2
    print(a+b)
add()'''

#def add(a,b,c):
 #   print(a+b+c)
#add(6,7,8)


'''def bio():
    var=input("enter your  name:")
    var1=int(input("enter your age as pr a proof:"))

    print(var)
    print(var1)
bio()'''


'''def data(name,rollno=102102):
    print(name)
    print(rollno)
data("ammamuthu")'''

#def sum(a,*b):
 #   for k in b:
  #      a=a+k
   # print(a)
#sum(1,2,3,4,5,6,7,8)

def person(name,**details):
    print("NAME",name)
    print(details["age"])
person("ammu",age=21,salary=200000,native="tvl")