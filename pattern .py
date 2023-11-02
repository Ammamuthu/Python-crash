print("Enter how many pattern do you want :")
row=int(input())
print("enter a number 0 or 1 only these two chices :")
pattern=int(input())
change=bool(input(" "))
if change==True:
    for i in range(1,row+1):
        for j in range(1,i+1):
            print("*",end=" ")
    print()
elif change==False:
    for i in range(row,0,-1):
             print("#",end=" ")
    print()

# print("8\t\n 8\n \t8\n 8")
# print(8)
# print(8)
# print(8)
# print(8)
# print(8)
