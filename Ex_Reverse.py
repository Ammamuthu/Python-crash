# from typing import ValuesView


# var="Hello world"
# print(var)
# emp=""
# for i  in var:
#     emp=i+emp
# print(emp)


user=input("Enter The Text : ")
ans=user[::-1]
print(ans,"orginal",user)

val=""
for i in user:
    val=i+val           #empty=H+empty==>h
                            
print(val)

