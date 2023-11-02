print("Entr your first number")
var1=input()
print("Enter your second number")
var2=input()
try:
    print("sum of a valuue is",int(var1)+int(var2))
except Exception as k:
    print("whatevr it takes")
    print(k)    