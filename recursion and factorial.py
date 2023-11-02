x= int(input("entr the number hat you whant bto factorial :")
def factorial(x):
    if x==0:
        return 1
    return x*factorial(x-1)
sum=factorial(100)
print(sum)