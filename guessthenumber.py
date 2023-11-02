var=9
i=1
while i<=10:
    print("enter th my dob")
    k=int(input())
    if k>var:
        print(" no man your not correct ,just little lower")
    elif k<var:
        print("no maan just bigger than that")
    elif k==var:
        print(" yo!! you always correct")
        print("you have won in ",i,"life")
        break
    print(10-i,"life left")
    i=i+1
if i>10:
        print("shit!!!!!here we go again")

