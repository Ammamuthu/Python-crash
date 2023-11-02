print("\n")

for i in range(0,7):
    for j in range(0,7):
        if (j==0 and i<=7) or (j==1 and i==0) or (j==2 and i==0) or (j==3 and i==0)  or (j==4 and i==0) or (j==5 and i==0)  or (j==6 and i<=7)  or (i==4 and j==1) or (i==4 and j==2) or (i==4 and j==3) or (i==4 and j==4) or (i==4 and j==5):
            print("A",end=" ")
        else:
            print("  ",end="")
    print("\n")
     
     