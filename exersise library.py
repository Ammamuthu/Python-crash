import time
sss=time.strftime("%d/%m/%y")

print("_________________________________ WELCOM  To ONLINE libray_____________________________")
print("we have book based on programing")
print(" 1 . List of Book's")
print("2 . Lend a Book's")
print("3 . Add book's")
print("4.Return book's")
print("5 . Buy a book ")
user=int(input( "Enter number what should you nd that..?"))
if user==1:
    print("1.HTML")
    print("2.CSS")
    print("3.Python")
    print("4.3D modeillng")

elif user==2:
    print(f"which book you want to LEND{sss} ..press the button of Number : " )
    lend=int(input())
    if lend==1:
        print("you have sussesfully purxhased HTML")
    elif lend==2:
        print(" You have succsesfully Purchased CSS")
    elif lend==3:
        print("You have succsfully purchased PYTHON")
    elif lend ==4:
        print("You have succesfullly purchased 3D Modelling")
    else:
        print("soory we dont't have that option")
           
           
elif user==3:
    book=input(" Enter the Book name ,that you want to add : ")
    print("succesfully added")
    print("1.HTML")
    print("2.CSS")
    print("3.Python")
    print("4.3D modeillng")
    print("5.",book)
elif user==4:
    ret=input("Enter the book name : ")
    print(f"Th book was {ret} thankyou!!!!")
    
elif user==5:
    print("1.HTML---400$")
    print("2.CSS---- 200$")
    print("3.Python ----- 500$")
    print("4.3D modeillng------1200$")
    buy=int(input("Entr the num of book you want to Buy :"))
    if buy==1:
         print("You have suucesfully purchased HTML")
    elif buy==2:
        print("You have succesfully purchased CSS")
    elif buy==3:
         print("You have sucessfully purchased PYTHON")
    elif buy==4:
         print("You have succesfully purchased 3D Modelling")
            
           