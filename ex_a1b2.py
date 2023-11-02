# a1b2b3



inbut="a5b6z4"

outbut=""

for i in  inbut:
    if i.isalpha():
        ans=i

    else:
        d=int(i)
        outbut=outbut+ans*d

print(outbut)


textt="one two hre"
emp=""

b=textt[::-1]
print(b)


for k in textt:
    emp=k+emp
print(emp)