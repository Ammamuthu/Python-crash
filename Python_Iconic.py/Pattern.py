# for i in range(0,5+1):
#     for j in range(0,i):
#         print("@ ",end="")
     
#     print("\n")


# print("\n")
# rvrsed pattern
# # 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

# for i in range(0,5):
#     for j in range(0,i):
#         print("&")

# n=6
# d=2*n-2
# for i in range(6,0,-1):
#     for j in range(0,d):
#         print("g",end=" ")
#     for k in range(0,i):
#         print("@",end=" ")
#     print("\r")




# print NNNNNNNNNNNNNN

for i in range(0,7):
    for j in range(0,7):
        if (j==0 and i<=7) or (j==6 and i<=7) or (j==1 and i==1) or (j==2 and i==2) or (j==3 and i==3) or (j==4 and i==4) or (j==5 and i==5) :
            print("N",end=" ")
        else:
            print("  ",end="")

    print("\r")
   

 
print("\n")
for i in range(0,7):
    for j in range(0,7):
        if (j==0 and i<=7) or (j==1 and i==0) or (j==2 and i==0) or (j==3 and i==0)  or (j==4 and i==0) or (j==5 and i==0)  or (j==6 and i<=7)  or (i==4 and j==1) or (i==4 and j==2) or (i==4 and j==3) or (i==4 and j==4) or (i==4 and j==5):
            print("A",end=" ")
        else:
            print("  ",end="")

    print("\r")

